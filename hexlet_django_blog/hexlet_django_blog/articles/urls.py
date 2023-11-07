from django.urls import path

from hexlet_django_blog.articles import views


urlpatterns = [
    path('', views.IndexArticlesView.as_view()),
    path('<str:tags>/<int:article_id>/', views.index, name='article'),
]
