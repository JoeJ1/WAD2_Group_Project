from django import forms
from django.contrib.auth.models import User

from chat.models import UserProfile, Chat, File
from django.contrib.auth.forms import UserChangeForm


class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username','password')


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('display_name', 'picture')


class ChatForm(forms.ModelForm):
    name = forms.CharField(max_length=100, help_text="Please enter the chat name.")
    description = forms.CharField(max_length=300, help_text="Please enter a description of the chat.") # far from finished but made a start 
    image = forms.ImageField(required=False)
    users = forms.ModelMultipleChoiceField(queryset=UserProfile.objects.all())
    owner = forms.ModelChoiceField(queryset=UserProfile.objects.all())

    class Meta:
        model = Chat
        fields = ('name', 'description', 'image', 'users', 'owner')
        
class FileForm(forms.ModelForm):
    
    class Meta:
        model = File
        #need to fix name as it gets overwritten with actual file name
        
        
        #to bootstrap
        # widgets = {
        #     'data': forms.FileField(attrs= {'class':'form-control'})
        # }
        # can do the same to make labels with a labels dict
        
        fields = ['data'] 
        
class ChangeUserDisplayName(forms.ModelForm):
    class Meta:
        model = UserProfile
        widgets = {
            'display_name' : forms.TextInput(attrs= {'class':'form-control mt-2', 'placeholder' : 'Enter a new display name.'})
        }

        labels = {
            'display_name' : ''
        }
        fields = ['display_name']
        
  
class ChangeUserProfilePic(forms.ModelForm):
    class Meta:
        model = UserProfile
        widgets = {
            'picture' : forms.ClearableFileInput(attrs= {'class':'form-control mt-2', 'placeholder' : 'Upload a new profile picture'})
        }
        fields = ['picture']
        labels = {
            'picture' : ''
        }
