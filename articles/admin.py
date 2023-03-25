from django.contrib import admin
from articles.models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    list_display = ('title', 'user', 'date_created', 'date_updated')
    list_filter = ('date_created', )

    list_select_related = ('user',)
    readonly_fields = ('user', )

    fields = (('title', 'body'), 'image', list_select_related)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)


