from django import forms
from todoapp.models import Todos

class todoform(forms.ModelForm):
    class Meta:
        model=Todos
        fields=["title","description"]
        widgets={
            "title":forms.TextInput(attrs={"class":"form-control","placeholder":"title"}),
            "description":forms.TextInput(attrs={"class":"form-control","placeholder":"description"}),
        }

class todoeditform(forms.ModelForm):
    class Meta:
        model=Todos
        fields=["title","description","status"]
        widgets={
            "title":forms.TextInput(attrs={"class":"form-control","placeholder":"title"}),
            "description":forms.TextInput(attrs={"class":"form-control","placeholder":"description"}),
            "status":forms.CheckboxInput(attrs={"class":"form-check-input"}),
        }


