# from django.shortcuts import render
from django.views.generic import View


# Create your views here.
class IndexView(View):
    template_name = 'articles/index.html'
