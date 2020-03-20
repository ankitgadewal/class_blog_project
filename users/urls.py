from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('reg', views.reg),
    path('login', views.login),
    path('checklogin', views.checklogin)
]