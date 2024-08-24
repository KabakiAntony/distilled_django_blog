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
    path('<int:id>/', blog_detail, name='blog_detail'),
    path('new/', blog_create, name='blog_create'),
    path('<int:id>/edit/', blog_update, name='blog_update'),
    path('<int:id>/delete/', blog_delete, name='blog_delete'),
]
