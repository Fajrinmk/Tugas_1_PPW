from django import forms

class Status_Form(forms.Form):
    error_messages = {
        'required': 'Tolong isi input ini',
        
    }
    status_attrs = {
        'type': 'text',
        'cols' : 100,
        'rows' : 4,
        'class' : 'todo-form-textarea',
        'placeholder' : 'Apa yg km pikirin sist'
    }

   
    status = forms.CharField(label='',widget=forms.Textarea(attrs=status_attrs), required=True)