from django.shortcuts import render
from django.http import JsonResponse
from .models import InteriorDesign

def budget_estimator(request):
    return render(request, 'budget_estimator/budget_estimator.html')

def calculate_budget(request):
    if request.method == 'POST' and request.is_ajax():
        design_style = request.POST.get('design_style')
        components = InteriorDesign.objects.all()
        total_cost = 0

        for component in components:
            if design_style == 'modern':
                total_cost += component.modern_price
            elif design_style == 'classic':
                total_cost += component.classic_price
            elif design_style == 'minimalist':
                total_cost += component.minimalist_price
            elif design_style == 'bohemian':
                total_cost += component.bohemian_price

        return JsonResponse({'total_cost': total_cost, 'design_style': design_style})

    return JsonResponse({'error': 'Invalid request'}, status=400)