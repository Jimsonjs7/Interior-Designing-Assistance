# budget_estimator/views.py
from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import BudgetEstimate, DesignStyle, FlooringType
from .forms import BudgetEstimateForm

class BudgetEstimatorView(CreateView):
    model = BudgetEstimate
    form_class = BudgetEstimateForm
    template_name = 'budget_estimator.html'
    success_url = reverse_lazy('estimate_result')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Debugging: Print the queryset
        print("Design Styles:", DesignStyle.objects.all())
        print("Flooring Types:", FlooringType.objects.all())
        return context

def estimate_result(request):
    latest_estimate = BudgetEstimate.objects.latest('created_at')
    return render(request, 'estimate_result.html', {'estimate': latest_estimate})