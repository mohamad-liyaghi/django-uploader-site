from django import forms
from file.models import UserFile

class FileForm(forms.ModelForm):
    class Meta:
        model = UserFile
        fields = ("title","slug","owner","file")