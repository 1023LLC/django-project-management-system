from django import forms 
from .models import Todolist


class TodolistForm(forms.ModelForm):
    class Meta:
        model = Todolist
        fields = ['name', 'description']
        