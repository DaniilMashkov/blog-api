from django.urls import path

from articles.views import CommentListAPIView, ArticleCreateAPIView, ArticleListApiView, ArticleRetrieveAPIView, \
    ArticleUpdateAPIView, ArticleDestroyAPIView, CommentRetrieveAPIView, CommentUpdateAPIView, CommentDestroyAPIView, \
    CommentCreateAPIVIew

urlpatterns = [
    path('', ArticleListApiView.as_view(), name='articles'),
    path('create/', ArticleCreateAPIView.as_view(), name='create_article'),
    path('update/<int:pk>/', ArticleUpdateAPIView.as_view(), name='update_article'),
    path('delete/<int:pk>/', ArticleDestroyAPIView.as_view(), name='delete_article'),
    path('<int:pk>/', ArticleRetrieveAPIView.as_view(), name='retrieve_article'),

    path('comments/', CommentListAPIView.as_view(), name='comments'),
    path('comments/create/', CommentCreateAPIVIew.as_view(), name='create_comment'),
    path('comments/<int:pk>/', CommentRetrieveAPIView.as_view(), name='retrieve_comment'),
    path('comments/update/<int:pk>/', CommentUpdateAPIView.as_view(), name='update_comment'),
    path('comments/delete/<int:pk>/', CommentDestroyAPIView.as_view(), name='delete_comment')
    ]