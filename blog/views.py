from django.shortcuts import render, redirect
from .models import Category, Post
from django.utils import timezone
# from django.db import models


def Home(request):
    if request.method == 'GET':
        all_posts = Post.objects.all()
        return render(request, 'blog.html', {'all_posts' : all_posts})
    # return render(request, 'blog.html')

def add_post(request):
    categories = Category.objects.all() 
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        category_id = request.POST.get('category')
        if title and content and category_id:
            category = Category.objects.get(id=category_id)
            Post.objects.create(
                title=title,
                content=content,
                created_by=timezone.now(),
                category = category
            )
            return redirect('home')
    return render(request, 'add_post.html', {'categories': categories})


   

# def Updatepost():

# def Deletepost():



# def Comment_to_post():



# def category_list():

