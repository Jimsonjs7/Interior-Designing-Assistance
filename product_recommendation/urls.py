from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('online_recommendation/', views.online_recommendation, name='online_recommendation'),
    path('offline_recommendation/', views.offline_recommendation, name='offline_recommendation'),
    path('recommend/', views.upload_image, name='upload_image'),
    path('offline_map _recommendation/', views.offline_map_recommendation, name='offline_map _recommendation.html'),
    path('results/', views.results, name='results.html'),
    #path('login/', views.login, name='login'),
    #path('register/', views.register, name='register'),
   # path('about/', views.about, name='about'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)