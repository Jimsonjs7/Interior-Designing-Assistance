# budget_estimator/admin.py
from django.contrib import admin
from .models import DesignStyle, FlooringType

admin.site.register(DesignStyle)
admin.site.register(FlooringType)