from django.shortcuts import render, get_object_or_404
from django.views import View

from hexlet_django_blog.articles.models import Article


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


# class ArticleCommentsView(View):
#
#     def get(self, request, *args, **kwargs):
#         comment = get_object_or_404(Comment, id=kwargs['id'], article__id=kwargs['article_id'])
#
#         return render( ... )
