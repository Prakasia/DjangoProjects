from django import forms
from django.contrib.auth.models import User
from onboardingapp.models import EmployeeOnboardInfo

# Form section A — Account details (User)
class EmployeeOnboardingForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')

# Form section B — Onboarding details (Profile)
class EmployeeInfoForm(forms.ModelForm):
    class Meta():
        model = EmployeeOnboardInfo
        fields = ('profile_url','profile_img')

# Here We have two forms. From user it seems to be one single form. But are saved separately