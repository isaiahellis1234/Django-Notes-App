from django import forms

from .models import Note

from django.contrib.auth.models import User

class Note(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'body']