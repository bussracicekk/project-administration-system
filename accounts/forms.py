from django import forms
from django.contrib.auth import authenticate


class LoginForm(forms.Form):
    username = forms.CharField(max_length=15, label='User Name')
    password = forms.CharField(max_length=10, label='Password', widget=forms.PasswordInput)
    usertype = forms.CharField(max_length=10, label='User Type')

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        usertype = self.cleaned_data.get('usertype')
        if username and password:
            user = authenticate(username=username, password=password, useryype=usertype)
            if not user:
                raise forms.ValidationError('Username or password is not correct')
            return super(LoginForm, self).clean()

