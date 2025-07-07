from django.contrib import admin
from .models import Users, savedContacts, CallLog

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email", "password", "phone", "address", "joined_date")
    
class SavedContactAdmin(admin.ModelAdmin):    
    list_display = ("id", "owner", "username","email", "phone", "address", "saved_date")
    
class CallLogAdmin(admin.ModelAdmin):    
    list_display = ("id", "contact", "phone", "status", "time_spent", "date_called")

admin.site.register(Users, UserAdmin)
admin.site.register(savedContacts, SavedContactAdmin)
admin.site.register(CallLog, CallLogAdmin)