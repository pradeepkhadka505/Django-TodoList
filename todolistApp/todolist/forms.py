from django import forms
from django.forms import ModelForm 
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model: Task
        fields = "__all__"   # include all fields in forms
        #fields = ('title', 'completed') # include particular fieds of models in forms
