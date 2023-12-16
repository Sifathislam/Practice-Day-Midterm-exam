from django import forms
from .models import musician_model
from  django.contrib.auth.forms import UserCreationForm # to creatre an register form 
from django.contrib.auth.models import User
#This form is crearted for the resgistion  
class RegistationForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name','last_name','email']







# this form is created for the musician form 
class MusicainForm(forms.ModelForm):
    class Meta:
        model = musician_model
        fields = '__all__'


