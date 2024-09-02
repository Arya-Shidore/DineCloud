from django.contrib import admin
from .models import User, userProfile

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    readonly_fields = ("password",)
    list_display = ("first_name", "last_name", "username", "email", "phone_number", "role", "date_joined", "last_login", "is_admin", "is_staff", "is_active", "created_date", "modified_date")
    
admin.site.register(User, UserAdmin)
admin.site.register(userProfile)