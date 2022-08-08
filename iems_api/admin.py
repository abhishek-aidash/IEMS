from django.contrib import admin
from .models import *

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['department_name']

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ['status_name', 'department_name']
    
@admin.register(Enchroachment)
class EnchroachmentAdmin(admin.ModelAdmin):
    list_display = ['department_name', 'status_name', 'enchrt_id', 'enchrt_type', 'region', 'subregion', 'encrt_size', 'dist_from_center_of_asset', 'criticality']