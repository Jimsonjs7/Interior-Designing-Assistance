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

    path('classic/', views.classic, name='classic'),
    path('classic_bedroom/', views.classic_bedroom, name='classic_bedroom'),
    path('classic_kitchen/', views.classic_kitchen, name='classic_kitchen'),
    path('classic_bathroom/', views.classic_bathroom, name='classic_bathroom'),
    path('classic_livingroom/', views.classic_livingroom, name='classic_livingroom'),

    path('minimalist/', views.minimalist, name='minimalist'),
    path('minimalist_bedroom/', views.minimalist_bedroom, name='minimalist_bedroom'),
    path('minimalist_kitchen/', views.minimalist_kitchen, name='minimalist_kitchen'),
    path('minimalist_bathroom/', views.minimalist_bathroom, name='minimalist_bathroom'),
    path('minimalist_livingroom/', views.minimalist_livingroom, name='minimalist_livingroom'),

    path('bohemian/', views.bohemian, name='bohemian'),
    path('bohemian_bedroom/', views.bohemian_bedroom, name='bohemian_bedroom'),
    path('bohemian_kitchen/', views.bohemian_kitchen, name='bohemian_kitchen'),
    path('bohemian_bathroom/', views.bohemian_bathroom, name='bohemian_bathroom'),
    path('bohemian_livingroom/', views.bohemian_livingroom, name='bohemian_livingroom'),

    path('product-recommendation/<str:product_name>/', views.product_recommendation, name='product_recommendation'),
    path('product-recommendation/', views.product_recommendation, name='product_recommendation_no_name'),


    
   # path('login/', views.login, name='login'),
   # path('register/', views.register, name='register'),
   # path('about/', views.about, name='about'),
]