from django.contrib import admin
from django.utils.html import format_html

from .models import (
    Capture,
    CaloriesConsumption)


class CaptureAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'user', 'accuracy', 'calories', 'category', 'is_active', 'created_on')


class CaloriesConsumptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'food_item', 'quantity', 'calories', 'is_active', 'created_on')


admin.site.register(Capture, CaptureAdmin)
admin.site.register(CaloriesConsumption, CaloriesConsumptionAdmin)

