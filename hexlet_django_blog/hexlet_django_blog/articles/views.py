from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib import messages

from hexlet_django_blog.articles.models import Article, ArticleComment
from .forms import CommentArticleForm, ArticleForm


# Create your views here.
def index(request, tags=None, article_id=None):
    article_id = 42
    tags = 'python'

    return render(request, 'articles/index.html', context={'article_id': article_id, 'tags': tags})


class IndexArticleView(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(request, 'articles/index.html', context={
            'articles': articles,
        })

class ArticleView(View):

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        return render(request, 'articles/show.html', context={
            'article': article,
        })


class ArticleCommentFormView(View):

    def post(self, request, *args, **kwargs):
        form = CommentArticleForm(request.POST) # Получаем данные формы из запроса
        if form.is_valid(): # Проверяем данных формы на корректность
            form.save() # Сохраняем форму


class ArticleFormCreateView(View):

    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(request, 'articles/create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():  # Если данные корректные, то сохраняем данные формы
            form.save()
            messages.success(request, "Article created successfully!")
            return redirect('/articles/')  # Редирект на указанный маршрут
        # Если данные некорректные, то возвращаем человека обратно на страницу с заполненной формой
        messages.error(request, "It didn't save!")
        return render(request, 'articles/create.html', {'form': form})
