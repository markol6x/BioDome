from registration.forms import RegistrationForm
from django import forms
from django.contrib.auth import get_user_model
from . models import UserProfile

class UserProfileForm(forms.ModelForm):
    given_name = forms.CharField()
    middle_name = forms.CharField(required=False)
    surname = forms.CharField()
    institution = forms.CharField()
    class Meta:
        model = UserProfile
        fields = ('given_name', 'middle_name', 'surname', 'institution')


class UserRegistrationForm(RegistrationForm, UserProfileForm):
    class Meta():
        fields = ('username', 'given_name', 'middle_name', 'surname', 'institution', 'email', 'password1', 'password2')
        model = get_user_model()


class UpdateEmailForm(RegistrationForm):
    class Meta():
        fields = ('email', )
        model = get_user_model()
