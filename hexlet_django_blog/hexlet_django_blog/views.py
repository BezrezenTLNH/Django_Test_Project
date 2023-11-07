from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.urls import reverse


def index(request, tags=None, article_id=None):
    article_id = 42
    tags = 'python'

    return redirect(reverse('article', kwargs={'article_id': article_id, 'tags': tags}))


def about(request):
    tags = ['обучение', 'программирование', 'python', 'oop']
    return render(
        request,
        'about.html',
        context={'tags': tags},
    )
