from django.urls import path,include
from . import views
from django.contrib import admin
app_name = 'designs'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('modern/', views.modern, name='modern'),
    path('living-room-designs/', views.living_room_designs, name='living_room_designs'),
    path('product-recommendation/<str:product_name>/', views.product_recommendation, name='product_recommendation'),
    path('product-recommendation/', views.product_recommendation, name='product_recommendation_no_name'),


    
   # path('login/', views.login, name='login'),
   # path('register/', views.register, name='register'),
   # path('about/', views.about, name='about'),
]