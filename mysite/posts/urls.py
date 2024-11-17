from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    #path('polls/', include("polls.urls")),
    path('hhj/ttt', views.boobs),
    path('home/', views.home, name="home"),
    path("<int:id>", views.post)
]
