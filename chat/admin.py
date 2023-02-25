from django.contrib import admin
from chat.models import Chat, UserProfile, Message, File

admin.site.register(UserProfile)
admin.site.register(Chat)
admin.site.register(File)
admin.site.register(Message)
# Register your models here.
