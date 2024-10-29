from django.urls import path
from django.contrib.auth import views as auth_views

from .views import (
    blog_list,
    blog_detail, 
    blog_create,
    blog_update, 
    blog_delete,
    blog_register)

app_name = "blog"

urlpatterns = [
    path('', blog_list, name='blog_list'),
    path('<int:id>/', blog_detail, name='blog_detail'),
    path('new/', blog_create, name='blog_create'),
    path('<int:id>/edit/', blog_update, name='blog_update'),
    path('<int:id>/delete/', blog_delete, name='blog_delete'),
    path('register/', blog_register, name='blog_register'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
]

