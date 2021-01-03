from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from home_app.models import Office, Announcament


# NORMAL ACCOUNT FORM
# ---------------------------
class NormalAccountForm(forms.Form):
    username = forms.CharField(
        max_length=None, required=True, label='',
        widget=forms.TextInput(attrs={'placeholder': 'Username'})
    )
    email = forms.EmailField(
        max_length=None, required=True, label='',
        widget=forms.TextInput(attrs={'placeholder': 'Email'})
    )
    first_name = forms.CharField(
        max_length=None, required=True, label='',
        widget=forms.TextInput(attrs={'placeholder': 'First Name'})
    )
    last_name = forms.CharField(
        max_length=None, required=True, label='',
        widget=forms.TextInput(attrs={'placeholder': 'Last Name'})
    )
    password = forms.CharField(
        max_length=None, required=True, label='',
        widget=forms.TextInput(attrs={'placeholder': 'Password',
                                      'type': 'password'})
    )
    office_key = forms.CharField(
        max_length=20, required=True, label='',
        widget=forms.TextInput(attrs={'placeholder': 'Office Key',
                                      'type': 'password'})
    )


# OFFICE & ADMIN ACCOUNT FORM
# ---------------------------

TYPE_CHOICES = (
    ("JOURNALISM", "Journalism"),
)


class OfficeAccountForm(forms.Form):
    office_name = forms.CharField(
        max_length=None, required=True, label='',
        widget=forms.TextInput(attrs={'placeholder': 'Office Name'})
    )
    office_type = forms.ChoiceField(
        required=True, label='', choices=TYPE_CHOICES,
    )
    username = forms.CharField(
        max_length=None, required=True, label='',
        widget=forms.TextInput(attrs={'placeholder': 'Username'})
    )
    email = forms.EmailField(
        max_length=None, required=True, label='',
        widget=forms.TextInput(attrs={'placeholder': 'Email'})
    )
    first_name = forms.CharField(
        max_length=None, required=True, label='',
        widget=forms.TextInput(attrs={'placeholder': 'First Name'})
    )
    last_name = forms.CharField(
        max_length=None, required=True, label='',
        widget=forms.TextInput(attrs={'placeholder': 'Last Name'})
    )
    password = forms.CharField(
        max_length=None, required=True, label='',
        widget=forms.TextInput(attrs={'placeholder': 'Password',
                                      'type': 'password'})
    )


# LOGIN FORM
class LoginGateForm(forms.Form):
    username = forms.CharField(
        max_length=None, required=True, label='',
        widget=forms.TextInput(attrs={'placeholder': 'Username'})
    )
    password = forms.CharField(
        max_length=None, required=True, label='',
        widget=forms.TextInput(attrs={'placeholder': 'Password',
                                      'type': 'password'})
    )


# ANNOUNCAMENT FORM
class AnnouncamentForm(forms.Form):
    content = forms.CharField(
        max_length=1000, label='', required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Announce ...',
                                      'id': 'announcament-content'})
    )
