from django.shortcuts import render

from .models import Post

# Create your views here.

def starting_page(request):
    latest_posts = Post.objects.all()

    return render(request, "blog/index.html", {"posts": latest_posts})

def about_page(request):

    return render(request, "blog/about.html")

def contacts_page(request):

    return render(request, "blog/contacts.html")

def post_detail(request, slug):

    post_detail = Post.objects.get(slug=slug)

    return render(request, "post_detail.html", {"post_detail":post_detail})