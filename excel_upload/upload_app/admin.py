from django.contrib import admin
from .models import ExcelData

@admin.register(ExcelData)
class ExcelDataAdminModel(admin.ModelAdmin):
    """ ExcelData Admin Integration """
    list_display =["name", "age", "hobby"]
