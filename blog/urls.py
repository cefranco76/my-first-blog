"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', views.post_list, name='post_list'),
	path('post/<int:pk>/', views.post_detail, name='post_detail'),
	path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
	path('post/new', views.post_new, name='post_new'),
	path('post/<int:pk>/publish', views.post_publish, name='post_publish'),
	path('post/<int:pk>/remove', views.post_remove, name='post_remove'),
	path('drafts/', views.post_draft_list, name='post_draft_list'),
	path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
	path('accounts/logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
	
]