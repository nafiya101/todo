from django import forms
from django.contrib.auth.models import User


class userregisterform(forms.ModelForm):
    class Meta:
        model=User
        fields=["username","email","password"]


        widgets={
           "username":forms.TextInput(attrs={'class':'form-control'}),
           "email":forms.EmailInput(attrs={'class':'form-control'}) ,
           "password":forms.PasswordInput(attrs={'class':'form-control'}) ,
           
         }
        
class userloginform(forms.ModelForm):
    class Meta:
        model=User
        fields=["username","password"]

        widgets={
           "username":forms.TextInput(attrs={'class':'form-control'}),
           "password":forms.PasswordInput(attrs={'class':'form-control'}) ,
           
         }
        