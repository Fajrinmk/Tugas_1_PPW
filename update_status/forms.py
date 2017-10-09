from django import forms

class Status_Form(forms.Form):
    error_messages = {
        'required': 'Tolong isi input ini',
        'invalid': 'Isi input dengan email',
    }
    attrs = {
        'class': 'form-control'
    }

   
    status = forms.CharField(widget=forms.Textarea(attrs=attrs), required=True)