from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    inxclude = ('emergency contact',)
   

# Register your models here.
admin.site.register(Employee, EmployeeAdmin)
admin.site.unregister(Group)