from .views import index, about, article, user
from django.urls import path, include

app_name = 'blog'

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('article/<int:article_id>/', article, name='article'),
    path('user/<int:user_id>', user, name='user'),
]