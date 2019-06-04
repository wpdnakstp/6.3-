from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('newblog/', views.blogpost, name="newblog"),
    path('new/', views.new, name="new"),
    path('', views.index, name="indexx"),
    
    
]
