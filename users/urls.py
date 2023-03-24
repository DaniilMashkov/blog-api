from users.views import UserCreateAPIView, UserDestroyAPIView, UserListAPIView, UserUpdateAPIView, UserRetrieveAPIView
from django.urls import path


urlpatterns = [
    path('', UserListAPIView.as_view(), name='users'),
    path('create/', UserCreateAPIView.as_view(), name='create_user'),
    path('update/<int:pk>/', UserUpdateAPIView.as_view(), name='update_user'),
    path('delete/<int:pk>/', UserDestroyAPIView.as_view(), name='delete_user'),
    path('<int:pk>/', UserRetrieveAPIView.as_view(), name='retrieve_user')
    ]