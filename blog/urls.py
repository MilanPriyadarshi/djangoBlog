from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   path('',views.blog,name="blog"),
   path('postComment',views.postComment,name='postComment'),
   path('<str:slug>',views.blogPost,name="blogPost"),
   
]