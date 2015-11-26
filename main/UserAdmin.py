# Django system libraries
from django.contrib import admin
# Models
import UserModels

# ===== Users =====
# User admin module
class UserAdmin(admin.ModelAdmin):
    list_display = ("Email","Username")
    search_fields = ("Email","Username")
    list_per_page = 20

# Email validation records admin module
class EmailValidationRecordAdmin(admin.ModelAdmin):
    list_display = ("Email","Nonce")
    search_fields = ("Email",)
    list_per_page = 20

# Register admin module
admin.site.register(UserModels.User,UserAdmin)
admin.site.register(UserModels.EmailValidationRecord,EmailValidationRecordAdmin)