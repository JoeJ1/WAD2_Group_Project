import uuid
from django.db import models
from django.contrib.auth.models import User as DjangoUser
from django.template.defaultfilters import slugify
from django.utils import timezone
from allauth.account.signals import user_signed_up
from django.dispatch import receiver

USERNAME_LEN = 30
DISPLAY_NAME_LEN = 50
CHAT_NAME_LEN = 50
CHAT_DESCRIPTION_LEN = 240

class UserProfile(models.Model):
    user = models.OneToOneField(DjangoUser, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=50)
    picture = models.ImageField(upload_to = 'profile_images/', blank=True, default='profile_images/logo.png')

    def __str__(self):
        return self.user.username

class Chat(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=240)
    users = models.ManyToManyField(UserProfile, related_name="chats")
    owner = models.ForeignKey(UserProfile, on_delete = models.CASCADE, related_name= 'chats_owned')
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to = 'chat_images/', blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Chat, self).save(*args, **kwargs)
    def __str__(self):
        return self.name

class Message(models.Model):
    ID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    content = models.TextField()
    #display_name = models.ForeignKey(UserProfile,  on_delete= models.CASCADE, related_name = 'sender_name')#Why is this needed?
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(UserProfile, on_delete= models.CASCADE, related_name= 'sender')
    time_stamp = models.DateTimeField(default=timezone.now())

    def save(self,*args,**kwargs):
        self.time_stamp= timezone.now()
        super(Message,self).save(*args,**kwargs)

    def __str__(self):
        return f"\"{self.content}\""

class File(models.Model):
    ID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=256)
    data = models.FileField(upload_to = 'chat_files')
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        self.name = self.data.name
        super(File,self).save(*args,**kwargs)

@receiver(user_signed_up, sender=DjangoUser)
def user_signed_up(request, user, **kwargs):
    print(user)
    print(user.first_name)
    u=UserProfile.objects.get_or_create(user=user)[0]
    u.display_name=user.first_name+user.last_name
    u.save()
