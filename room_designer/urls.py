from django.urls import path
from . import views

urlpatterns = [
    path('ai_room_designer/', views.ai_room_designer, name='ai_room_designer'),
]