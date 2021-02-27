from django import forms
from .models import Usuario

class userForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'

class userLogin(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ()