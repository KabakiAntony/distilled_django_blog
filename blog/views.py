from django.shortcuts import render, redirect, get_object_or_404
from .models import Blogs
from .forms import BlogForm

def blog_list(request):
    posts = Blogs.objects.all()
    return render(request, 'blog/blog_list.html', {"posts":posts})

def blog_detail(request, id): 
    post = Blogs.objects.get(id)#before refactor
    # post = get_object_or_404(Blogs, id)
    return render(request, 'blog/blog_detail.html', {'post':post})

def blog_create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else: 
        form = BlogForm()
    return render(request, 'blog/blog_form.html', {'form':form})

def blog_update(request, id):
    post = get_object_or_404(Blogs, id)
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog_detail', id=post.id)
    else:
        form = BlogForm(instance=post)
    return render(request, 'blog/blog_form.html', {'form': form})

def blog_delete(request, id):
    post = get_object_or_404(Blogs, id)
    if request.method == 'POST':
        post.delete()
        return redirect('blog_list')
    return render(request, 'blog/blog_confirm_delete.html', {'post': post})