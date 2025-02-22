# budget_estimator/forms.py
from django import forms
from .models import BudgetEstimate, DesignStyle, FlooringType

class BudgetEstimateForm(forms.ModelForm):
    square_feet = forms.DecimalField(
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    design_style = forms.ModelChoiceField(
        queryset=DesignStyle.objects.all(),  # Ensure this is correct
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    flooring_type = forms.ModelChoiceField(
        queryset=FlooringType.objects.all(),  # Ensure this is correct
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = BudgetEstimate
        fields = ['square_feet', 'design_style', 'flooring_type']