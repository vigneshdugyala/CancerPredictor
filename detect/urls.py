from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    path('home',views.home,name="home"),path('start',views.start,name="start"),path('about',views.about,name="about"),
    path('home',views.home,name="start")
]
