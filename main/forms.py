from django import forms
from .models import StrayReport

class StrayReportForm(forms.ModelForm):
    class Meta:
        model = StrayReport
        fields = ['photo', 'location', 'description', 'latitude', 'longitude']
        widgets = {
            'latitude': forms.HiddenInput(),
            'longitude': forms.HiddenInput(),
        }
