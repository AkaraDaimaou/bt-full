from django.contrib import admin
from .models import Report
# Register your models here.

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('location', 'temperature', 'created_at')
    search_fields = ('location',)