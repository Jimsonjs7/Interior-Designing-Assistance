from django.urls import path
from . import views

urlpatterns = [
    path('modern/', views.modern, name='modern'),
    path('living_room_designs/', views.living_room_designs, name='living_room_designs'),
   # path('login/', views.login, name='login'),
   # path('register/', views.register, name='register'),
   # path('about/', views.about, name='about'),
]