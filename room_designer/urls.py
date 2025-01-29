from django.urls import path
from . import views
from .views import generate_image

urlpatterns = [
    path('results/', views.results, name='results'),
    path('room_designer/',views.ai_room_designer, name='ai_room_designer'),  # Home page
    path('generate/', views.generate_image, name='generate_image'),
]