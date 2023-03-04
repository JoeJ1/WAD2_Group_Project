from django.contrib import admin
from django.utils import timezone

from chat.models import Chat, UserProfile, Message, File

class ChatAdmin(admin.ModelAdmin):
    prepopulated_fields ={'slug':('name',)}

admin.site.register(UserProfile)
admin.site.register(Chat,ChatAdmin)
admin.site.register(File)
admin.site.register(Message)
# Register your models here.
