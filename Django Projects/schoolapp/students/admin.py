from django.contrib import admin

# Register your models here.
from .models import RegistrationForm

class RegistrationFormAdmin(admin.ModelAdmin):
    list_display = ('roll_no', 'registration_date', 'last_modified')
    list_filter = ('gender', 'last_modified')
    search_fields = ('roll_no',)


admin.site.register(RegistrationForm, RegistrationFormAdmin)