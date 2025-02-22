from django.urls import path
from .views import BudgetEstimatorView, estimate_result

urlpatterns = [
    path('estimate/', BudgetEstimatorView.as_view(), name='budget_estimator'),
    path('estimate/result/', estimate_result, name='estimate_result'),
]