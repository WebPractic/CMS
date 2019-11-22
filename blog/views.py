from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View
from .models import Category, Post

# def home(request):
#     if request.method == 'POST':
#         return HttpResponse('Hi')
#     elif request.method == 'GET':
#         return HttpResponse('Bye')


# class HomeView(View):
#
#     def get(self, request):
#         category_list = Category.objects.all()
#         return render(request, "blog/home.html", {"categories": category_list})

class HomeView(View):

    def get(self, request):
        post_list = Post.objects.all()
        return render(request, "blog/home.html", {"posts": post_list})


class CategoryView(View):
    """Вывод категории"""
    def get(self, request, category_name):
        category = Category.objects.get(slug=category_name)
        return render(request, "blog/post_list.html", {"category": category})


class PostView(View):
    """Вывод поста"""
    def get(self, request, post_name):
        post = Post.objects.get(slug=post_name)
        return render(request, "blog/post_detail.html", {"post": post})

