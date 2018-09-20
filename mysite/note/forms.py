from django import forms

from .models import Notes


class NoteForm(forms.ModelForm):
    link = Notes.link
    name = Notes.name
    class Meta:
        model = Notes
        fields = ('name', 'link', 'create_date')
