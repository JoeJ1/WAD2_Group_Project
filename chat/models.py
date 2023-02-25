import uuid
from django.db import models
from django.contrib.auth.models import User as DjangoUser

USERNAME_LEN = 30
DISPLAY_NAME_LEN = 50
CHAT_NAME_LEN = 50
CHAT_DESCRIPTION_LEN = 240

class UserProfile(models.Model):
    #username = models.CharField(max_length=30, unique=True, default=User.username)# django creates username automatically?
    user = models.OneToOneField(DjangoUser, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=50)
    picture = models.ImageField(upload_to = 'profile_images', blank=True)

    def __str__(self):
        return self.user.username

class Chat(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=240)
    users = models.ManyToManyField(UserProfile)
    owner = models.CharField(UserProfile, max_length=50)

    def __str__(self):
        return self.name

class Message(models.Model):
    ID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    content = models.CharField(max_length=1000)
    display_name = models.CharField(max_length=200)#Why is this needed?
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    sender = models.CharField(max_length=30)

    def __str__(self):
        return f"\"{self.content}\""

class File(models.Model):
    ID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=256) # Max file name length on windows
    expiry = models.DateTimeField('expiry')#Do we need an expiry? we could just delete when chat is deleted
    data = models.FileField(upload_to = 'chat_files') #change upload_to
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


