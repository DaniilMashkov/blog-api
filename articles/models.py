from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    image = models.ImageField(blank=True, null=True)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    body = models.CharField(max_length=254)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


