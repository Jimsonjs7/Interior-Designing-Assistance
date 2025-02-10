from django.urls import path
from . import views

urlpatterns = [
    path('', views.quiz_home, name='quiz_home'),
    path('result/', views.quiz_result, name='quiz_result'),
]
