from django import forms
from .models import File_upload

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = File_upload
        fields = ('file', )






