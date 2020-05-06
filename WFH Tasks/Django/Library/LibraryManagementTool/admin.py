from django.contrib import admin

# Register your models here.
from .models import Books

class BooksAdmin(admin.ModelAdmin):
    list_display = ('isbn','title','author','genere','available')
    actions = ('mark_as_available', 'mark_as_unavailable', 'Stock_Sold')
    search_fields = ('isbn','title','author','genere')

    def mark_as_unavailable(self, request, queryset):
        count = queryset.update(available=False)
    
    def mark_as_available(self, request, queryset):
        count = queryset.update(available=True)
    
    def Stock_Sold(self, request, queryset):
            count = queryset.update(quantity = 0)
            count = queryset.update(available = False)
        
admin.site.register(Books, BooksAdmin)
