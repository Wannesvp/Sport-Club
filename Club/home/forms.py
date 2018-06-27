from django import forms
from django.contrib.auth.models import User
from home.models import Profile, Training, Warm_up, Core, Cool_down
from django.forms.widgets import CheckboxSelectMultiple

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
        fields = ('name', 'is_standard', 'date', 'start_time', 'end_time','location', 'trainers', 'riders', 'warm_up', 'core', 'cool_down')

    def __init__(self, *args, **kwargs):
        
        super(TrainingForm, self).__init__(*args, **kwargs)
        self.fields["trainers"].widget = CheckboxSelectMultiple()
        self.fields["trainers"].queryset = Profile.objects.all()
        self.fields["riders"].widget = CheckboxSelectMultiple()
        self.fields["riders"].queryset = Profile.objects.all()

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
