from django import forms
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import InMemoryUploadedFile

class UserBioForm(forms.Form):
    name = forms.CharField(max_length=100)
    age = forms.IntegerField(label="Your age", min_value=1, max_value=99)
    bio = forms.CharField(label="Biography", widget=forms.Textarea, max_length=300)
    
def validate_size(file: InMemoryUploadedFile):
    max_size = 1   
    if file.size / 1048576 > max_size:
        raise ValidationError(f"File size error! File bigger than {max_size} mb")
    
class UploadFileForm(forms.Form):
    file =forms.FileField(validators=[validate_size])