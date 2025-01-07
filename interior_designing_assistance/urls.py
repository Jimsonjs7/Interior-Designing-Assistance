from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('homeloggedin/', views.homeloggedin, name='homeloggedin'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('viewprofile/', views.viewprofile, name='viewprofile'),
    path('updateprofile/', views.updateprofile, name='updateprofile'),
]