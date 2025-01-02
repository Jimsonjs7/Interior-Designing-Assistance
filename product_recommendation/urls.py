from django.urls import path
from . import views

urlpatterns = [
    path('online_recommendation/', views.online_recommendation, name='online_recommendation'),
    path('offline_recommendation/', views.offline_recommendation, name='offline_recommendation'),
    path('upload_image/', views.upload_image, name='upload_image'),
    #path('login/', views.login, name='login'),
    #path('register/', views.register, name='register'),
   # path('about/', views.about, name='about'),
]