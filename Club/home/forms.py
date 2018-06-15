from django import forms
from django.contrib.auth.models import User
from home.models import Profile, Training

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'location', 'birth_date')


class TrainingForm(forms.ModelForm):
    class Meta:
        model = Training
        fields = ('name', 'date', 'start_time','location', 'warm_up', 'core', 'cool_down')