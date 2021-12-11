from .models import Profile,Project
from django.forms import ModelForm
from django import forms

class PostProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ('image',
                   'project_name',
                   'description',
                   'category',
                   'location',
                   'url',
        )

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'prof_photo','phone_number')

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']