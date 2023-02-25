from django import forms
from django.contrib.auth.models import User

from rango.models import UserProfile


class UserForm(forms.modelForm):
    password = forms.CharField(widget = forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username','password')


class UserProfileForm(forms.modelForm):

    class Meta:
        model = UserProfile
        fields = ('display_name', 'picture')