from django.contrib import admin
from .models import OpeningHour,Vendor
# Register your models here.

class vendorAdmin(admin.ModelAdmin):
    list_display = ('vendor_name', 'vendor_license','created_at')
    search_fields = ('vendor_name', 'vendor_license')
    


admin.site.register(OpeningHour)
admin.site.register(Vendor, vendorAdmin)