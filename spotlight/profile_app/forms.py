from django import forms
from django.forms import ModelForm
from profile_app.models import ProfileSettings


# SETTINGS FROM
class ProfileSettingsForm(ModelForm):
    class Meta:
        model = ProfileSettings
        fields = ['profile_photo', 'bio', 'personal_link']
        widgets = {
            "bio": forms.TextInput(
                attrs={'placeholder': 'Bio ...', 'class': 'settings_input',
                       'id': 'bio', }
            ),
            "personal_link": forms.TextInput(
                attrs={'placeholder': 'Personal URL', 'id': 'personal_link',
                       'class': 'settings_input', }
            ),
        }
