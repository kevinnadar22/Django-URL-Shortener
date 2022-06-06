from django import forms
from .models.urls_model import Urls

class UrlForm(forms.ModelForm):

    class Meta:
        model = Urls
        fields = ('long_url',) 
        widgets = {
        'long_url': forms.URLInput(attrs={
            'class': 'form-control',
            'placeholder':'Enter a long URL',
            'name': 'long_url',
        }),
        }

    def customSave(self):
        lv = self.save()
        return lv
