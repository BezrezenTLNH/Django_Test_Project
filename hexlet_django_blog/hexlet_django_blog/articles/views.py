from django.shortcuts import render
from django.views import View
from django.http import HttpResponse


# Create your views here.
def index(request, tags=None, article_id=None):
    article_id = 42
    tags = 'python'

    return render(request, 'articles/index.html', context={'article_id': article_id, 'tags': tags})


class IndexArticlesView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('I hate this Hexlet lessons')

