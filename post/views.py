from django.shortcuts import render, redirect
from .models import Post, Course
from .forms import PostForm
# Create your views here.


def post_view(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'post_list.html', context)

def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return render(request, 'post_create.html', {'form': form})
    else:
        form = PostForm()
    return render(request, 'post_create.html', {'form': form})


def course_view(request):
    courses = Course.objects.all()
    context = {
        'courses': courses
    }
    return render(request, 'courses.html', context)
