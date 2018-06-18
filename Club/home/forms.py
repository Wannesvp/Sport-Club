from django import forms
from django.contrib.auth.models import User
from home.models import Profile, Training, Warm_up, Core, Cool_down

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


class Warm_upForm(forms.ModelForm):
    class Meta:
        model = Warm_up
        fields = '__all__'

class CoreForm(forms.ModelForm):
    class Meta:
        model = Core
        fields = '__all__'


class Cool_downForm(forms.ModelForm):
    class Meta:
        model = Cool_down
        fields = '__all__'
