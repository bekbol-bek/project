from django.urls import path
from . import views
from .views import article_search

urlpatterns = [
    path('', views.article_list, name='article_list'),  # Список статей
    path('article/<int:article_id>/', views.article_detail, name='article_detail'),  # Отдельная статья
    path('article/new/', views.article_create, name='article_create'),  # Добавить статью
    path('article/<int:article_id>/edit/', views.article_update, name='article_update'),  # Редактировать статью
    path('article/<int:article_id>/delete/', views.article_delete, name='article_delete'),
    path('search/', article_search, name='article_search'),
    # Удалить статью
]