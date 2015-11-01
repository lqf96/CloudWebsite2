# Django system libraries
from django.contrib import admin
# Models
import DZModels,UserModels

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

# ===== Discussion Zone =====
# Discussion zone boards admin module
class DiscussionZoneBoardAdmin(admin.ModelAdmin):
    list_display = ("Name","PostAmount")
    search_fields = ("Name",)
    list_per_page = 20

# Discussion zone posts admin module
class DiscussionZonePostAdmin(admin.ModelAdmin):
    list_display = ("PostID","Title","Board","Author","Time","LastReply","LastReplyTime","ReplyAmount")
    search_fields = ("PostID","Title","Board","Author","Time")
    list_per_page = 20

# Discussion zone post content admin module
class DiscussionZoneContentAdmin(admin.ModelAdmin):
    list_display = ("PostID","ContentID","Board","Author","Time")
    search_fields = ("PostID","ContentID","Board","Author","Time")
    list_per_page = 20

# Register admin module
admin.site.register(DZModels.DiscussionZoneBoard,DiscussionZoneBoardAdmin)
admin.site.register(DZModels.DiscussionZoneContent,DiscussionZoneContentAdmin)
admin.site.register(DZModels.DiscussionZonePost,DiscussionZonePostAdmin)
