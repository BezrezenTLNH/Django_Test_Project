from django.urls import path

from hexlet_django_blog.articles.views import (IndexArticleView,
                                              ArticleView)


urlpatterns = [
    path('', IndexArticleView.as_view()),
    path('<int:id>/', ArticleView.as_view(), name='article_show'),
]
