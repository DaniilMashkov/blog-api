from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from .models import User


@admin.register(User)
class UserAdmin(DjangoUserAdmin):

    list_display = ('username', 'email', 'birthdate', 'date_updated', 'is_staff')
    search_fields = ('username', 'birthdate', 'date_updated')
    ordering = ('username',)
