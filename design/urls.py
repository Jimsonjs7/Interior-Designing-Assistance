from django.urls import path,include
from . import views
from django.contrib import admin
app_name = 'designs'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('modern/', views.modern, name='modern'),
    path('modern_bedroom/', views.modern_bedroom, name='modern_bedroom'),
    path('modern_kitchen/', views.modern_kitchen, name='modern_kitchen'),
    path('modern_bathroom/', views.modern_bathroom, name='modern_bathroom'),
    path('modern_living-room-designs/', views.modern_living_room_designs, name='modern_living_room_designs'),
    path('product-recommendation/<str:product_name>/', views.product_recommendation, name='product_recommendation'),
    path('product-recommendation/', views.product_recommendation, name='product_recommendation_no_name'),


    
   # path('login/', views.login, name='login'),
   # path('register/', views.register, name='register'),
   # path('about/', views.about, name='about'),
]