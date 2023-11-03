from django.shortcuts import render


# Create your views here.
def index(request):
    name = 'hexlet_django_blog.article'
    return render(request, 'articles.html', context={'name': name})
