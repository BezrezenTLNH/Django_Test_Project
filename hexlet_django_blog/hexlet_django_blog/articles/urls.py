from django.urls import path

from hexlet_django_blog.articles.views import (IndexArticleView,
                                              ArticleView, ArticleCommentFormView,
                                               ArticleFormCreateView,
                                               ArticleFormEditView,
                                               ArticleFormDeleteView)


urlpatterns = [
    path('', IndexArticleView.as_view(), name='article_index'),
    path('<int:id>/delete/', ArticleFormDeleteView.as_view(), name='articles_delete'),
    path('<int:id>/edit/', ArticleFormEditView.as_view(), name='articles_update'),
    path('<int:id>/', ArticleView.as_view(), name='article_show'),
    path('<int:article_id>/comments/<int:id>/', ArticleCommentFormView.as_view(), name='article_comment'),
    path('create/', ArticleFormCreateView.as_view(), name='articles_create'),
]
