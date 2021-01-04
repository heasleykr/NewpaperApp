from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

# Our classes inherit from the UserCreationForms, but we are going to customize & add functionality. 
# We are adding 'age'

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        #appending to a tuple with appending another tuple to create a new one. Tuples are immutable (unchangeable), so you must make a new one. 
        # fields = UserCreationForm.Meta.fields + ('age', 'nice_name',) 
        fields = UserCreationForm.Meta.fields + ('username', 'email', 'age',)
        # fields = UserCreationForm.Meta.fields + ('username','email','age',)

class CustomUserChangeForm(UserChangeForm):
        #Meta means 'about itself'
    class Meta(UserChangeForm):
        model = CustomUser
        # fields = UserChangeForm.Meta.fields
        fields = ('username', 'email', 'age',)