from django.urls import path

from .views import (
    blog_create, 
    blog_delete, 
    blog_detail, 
    blog_list,
    blog_update)

app_name = "blog"

urlpatterns = [
    path('', blog_list, name='blog_list'),
    path('create/', blog_create, name='blog_create'),
    path('read/<int:id>/', blog_detail, name='blog_detail'),
    path('delete/<int:id>/', blog_delete, name='blog_delete'),
    path('update/<int:id>/', blog_update, name='blog_update'),
]
