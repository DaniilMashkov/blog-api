from rest_framework import generics
from rest_framework.permissions import AllowAny

from articles.serializers import Article, ArticleSerializer, Comment, CommentSerializer


class ArticleCreateAPIView(generics.CreateAPIView):
    serializer_class = ArticleSerializer


class ArticleListApiView(generics.ListAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    permission_classes = [AllowAny, ]


class ArticleRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    permission_classes = [AllowAny, ]


class ArticleUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ArticleSerializer

    def get_queryset(self):

        if self.request.user.is_staff:
            return Article.objects.all()
        return Article.objects.filter(user=self.request.user)


class ArticleDestroyAPIView(generics.DestroyAPIView):
    serializer_class = ArticleSerializer

    def get_queryset(self):

        if self.request.user.is_staff:
            return Article.objects.all()
        return Article.objects.filter(user=self.request.user)


class CommentCreateAPIVIew(generics.CreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class CommentListAPIView(generics.ListAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [AllowAny, ]


class CommentRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [AllowAny, ]


class CommentDestroyAPIView(generics.DestroyAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):

        if self.request.user.is_staff:
            return Comment.objects.all()
        return Comment.objects.filter(user=self.request.user)


class CommentUpdateAPIView(generics.UpdateAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):

        if self.request.user.is_staff:
            return Comment.objects.all()
        return Comment.objects.filter(user=self.request.user)