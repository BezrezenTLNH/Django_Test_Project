from django.urls import path

from hexlet_django_blog.articles.views import (IndexArticleView,
                                              ArticleView, ArticleCommentFormView,
                                               ArticleFormCreateView)


urlpatterns = [
    path('', IndexArticleView.as_view()),
    path('<int:id>/', ArticleView.as_view(), name='article_show'),
    path('<int:article_id>/comments/<int:id>/', ArticleCommentFormView.as_view(), name='article_comment'),
    path('create/', ArticleFormCreateView.as_view(), name='articles_create'),
]
