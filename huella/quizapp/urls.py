from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('welcome/', views.welcome, name='welcome'),
    path('quiz/', views.quiz, name='quiz'),
    path('restult/', views.result, name='result'),
]