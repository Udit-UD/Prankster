from django.contrib import admin
from django.urls import path,include
from prank import views

urlpatterns = [
    path("",views.index,name="index"),
    path("result", views.result, name="result"),
    path("search", views.search, name= "search")
]