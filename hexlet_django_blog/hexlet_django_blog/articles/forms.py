from django import forms
from django.forms import ModelForm
from hexlet_django_blog.articles.models import ArticleComment
from .models import Article


class CommentArticleForm(forms.Form):
    content = forms.CharField(label='Комментарий') # Текст комментария


class ArticleCommentForm(ModelForm):
    class Meta:
        model = ArticleComment
        fields = ['content']


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['name', 'body']

