from django import forms
from .models import quickquery, enquiry

class quickqueryForm(forms.ModelForm):
 class Meta: 
  model = quickquery
  fields =  ['qname','qemail','qmessage']
  widget = {
   'name': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your name'}),
   'email': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your email'}),
   'message': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your message'}),
  }

class enquiryForm(forms.ModelForm):
 class Meta: 
  model = enquiry
  fields =  ['name','mobile','email','message']
  widget = {
   'name': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your name'}),
   'mobile': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your mobile'}),
   'email': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your email'}),
   'message': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your message'}),
  }