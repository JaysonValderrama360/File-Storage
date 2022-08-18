from django import forms
import datetime

class FileUploadForm(forms.Form):
    file_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    date_recieved = forms.DateField(widget=forms.DateInput(attrs={'class': "form-control", 'style': 'max-width: 300px;','placeholder': 'MM/DD/YYYY','type' : "date"}))
    status = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    protocol = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    notes = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_touched = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    file = forms.FileField(widget=forms.FileInput(attrs={'class':'form-control'}))
