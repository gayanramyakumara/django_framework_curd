from django.urls import path
from .views import get_users, create_user, user_detail_by_pk

urlpatterns = [
  path('users/', get_users, name='get_users'),
  path('users/create', create_user, name='create_user'),
  path('users/<int:pk>/', user_detail_by_pk, name='user_detail'),
]