from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm

class CustomUserEditForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'phone_number', 'profile_picture', 'position', 'department')
        