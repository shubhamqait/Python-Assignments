from django.contrib import admin

# Register your models here.
from .models import RegistrationForm


admin.site.site_header = 'Admin Dashboard'
admin.site.register(RegistrationForm)