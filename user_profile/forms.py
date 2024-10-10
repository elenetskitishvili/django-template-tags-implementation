
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label='Name')
    email = forms.EmailField(max_length=100, required=True, label='Email')
