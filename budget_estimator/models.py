# budget_estimator/models.py
from django.db import models
from django.core.validators import MinValueValidator

class DesignStyle(models.Model):
    name = models.CharField(max_length=100)
    cost_per_sqft = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name

class FlooringType(models.Model):
    name = models.CharField(max_length=100)
    cost_per_sqft = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name

class BudgetEstimate(models.Model):
    square_feet = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        validators=[MinValueValidator(1)]
    )
    design_style = models.ForeignKey(DesignStyle, on_delete=models.CASCADE)
    flooring_type = models.ForeignKey(FlooringType, on_delete=models.CASCADE)
    total_estimate = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def calculate_estimate(self):
        base_cost = float(self.square_feet) * float(self.design_style.cost_per_sqft)
        flooring_cost = float(self.square_feet) * float(self.flooring_type.cost_per_sqft)
        total = base_cost + flooring_cost
        total *= 1.1  # Add 10% for miscellaneous expenses
        return round(total, 2)

    def save(self, *args, **kwargs):
        self.total_estimate = self.calculate_estimate()
        super().save(*args, **kwargs)