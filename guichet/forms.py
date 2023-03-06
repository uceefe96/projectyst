from django import forms

class LoginForm(forms.Form):
    cne = forms.CharField(max_length=10)
    cin = forms.CharField(max_length=12, widget=forms.PasswordInput)
