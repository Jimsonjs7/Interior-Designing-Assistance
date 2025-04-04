from django.urls import path
from . import views

urlpatterns = [
    path('', views.budget_estimator, name='budget_estimator'),
    path('calculate-budget/', views.calculate_budget, name='calculate_budget'),
]