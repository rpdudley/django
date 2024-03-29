from django import forms
from hello.models import LogMessage
from django.forms import ModelForm
from .models import Poll
from .models import Employee
from django.contrib.auth.models import User

class LogMessageForm(forms.ModelForm):
    class Meta:
        model = LogMessage
        fields = ("message",)   # NOTE: the trailing comma is required
class CreatePollForm(ModelForm):
    class Meta:
        model = Poll
        fields = ['question', 'option_one', 'option_two', 'option_three']

class EmployeeForm(forms.ModelForm): 
    class Meta: 
        model = Employee 
        fields = ['name', 'emp_image']
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']