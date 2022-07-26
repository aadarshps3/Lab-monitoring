from django import forms
from django.contrib.auth.forms import UserCreationForm,forms,User


from .models import *


class TUserCreationForm(UserCreationForm):


    class Meta(UserCreationForm.Meta):
        model=RtUser
        fields=UserCreationForm.Meta.fields+('ip_address','system_name','client_name','email','phone','image')



