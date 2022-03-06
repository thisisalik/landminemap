from django.forms import ModelForm, widgets
from django import forms 
from .models import Mine, Location

class MineForm(ModelForm):
    class Meta:
        model=Mine
        fields="__all__"

class LocForm(ModelForm):
    class Meta:
        model=Location
        fields='__all__'