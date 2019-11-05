from django.urls import path

from .views import ArticleDeleteView,ArticleUpdateView,ArticleListView,ArticleCreateView,ArticleDetailView


urlpatterns=[
    path('<int:pk>/edit/',ArticleUpdateView.as_view(), name='article_update'),
    path('<int:pk>/delete/',ArticleDeleteView.as_view(), name='article_delete'),
    path('new/',ArticleCreateView.as_view(), name='article_create'),
    path('<int:pk>/',ArticleDetailView.as_view(), name='article_detail'),
    path('',ArticleListView.as_view(),name= 'article_list'),
    ]
