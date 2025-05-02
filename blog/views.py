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