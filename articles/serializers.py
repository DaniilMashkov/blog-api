from rest_framework import serializers
from articles.models import Article, Comment
from articles.validators import ArticleValidator


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Comment
        fields = ['body', 'article', 'date_updated', 'user']


class ArticleSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    comments = CommentSerializer(source='comment_set', many=True, read_only=True)

    class Meta:
        model = Article
        fields = '__all__'
        validators = [ArticleValidator(field='model')]

