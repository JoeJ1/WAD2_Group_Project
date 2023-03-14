from django import forms
from django.contrib.auth.models import User

from chat.models import UserProfile, Chat


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