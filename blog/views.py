from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Blogs
from .forms import BlogForm, UserRegisterForm


def blog_list(request):
    posts = Blogs.objects.all().order_by('-created_at')
    return render(request, 'blog/blog_list.html', {"posts":posts})

def blog_detail(request, id):
    post = Blogs.objects.get(id=id)
    return render(request, 'blog/blog_detail.html', {'post':post})

@login_required
def blog_create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog:blog_detail', id=post.id)
    else: 
        form = BlogForm()
    return render(request, 'blog/blog_form.html', {'form':form})

@login_required
def blog_update(request, id):
    post = Blogs.objects.get(id=id)

    if post.author != request.user:
        return HttpResponseForbidden("You are not allowed to edit this post.")
    
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog:blog_detail', id=post.id)
    else:
        form = BlogForm(instance=post)
    return render(request, 'blog/blog_form.html', {'form': form})

@login_required
def blog_delete(request, id):
    post = Blogs.objects.get(id=id)

    if post.author != request.user:
        return HttpResponseForbidden("You are not allowed to delete this post.")
    
    if request.method == 'POST':
        post.delete()
        return redirect('blog:blog_list')
    return render(request, 'blog/blog_confirm_delete.html', {'post': post})

def blog_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('blog:blog_list')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})
        