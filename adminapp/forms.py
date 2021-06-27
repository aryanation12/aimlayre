from django import forms
from django.db.models import fields
from django.forms import widgets
from app.models import Student, business, referral, quickquery, enquiry



class StudentForm(forms.ModelForm):
 class Meta:
  model = Student
  fields = ['Image1', 'Image2', 'Image3','aboutimage1','aboutimage2','aboutimage3','aboutimage4','aboutimage5','aboutimage6','aboutimage7','aboutcontent','servicecontent','solution','succestory1','succestory2','successimage1','successimage2','contact']
  widgets = {
   'aboutcontent': forms.Textarea(attrs={'class':'form-control','placeholder':'Enter about content', 'size':50}),
   'servicecontent': forms.Textarea(attrs={'class':'form-control','placeholder':'Enter service content','size':50}),
   'solution': forms.Textarea(attrs={'class':'form-control','placeholder':'Enter solution content','size':50}),
   'succestory1': forms.Textarea(attrs={'class':'form-control','placeholder':'Enter success story','size':50}),
   'succestory2': forms.Textarea(attrs={'class':'form-control','placeholder':'Enter success story','size':50}),
   
   }


class BusinessForm(forms.ModelForm):
 class Meta:
  model = business
  fields = ['Image1', 'Image2', 'Image3','aboutimage1','aboutimage2','aboutimage3','aboutimage4','aboutimage5','aboutimage6','aboutimage7','aboutcontent','servicecontent','solution','succestory1','succestory2','successimage1','successimage2','contact']
  widgets = {
   'aboutcontent': forms.Textarea(attrs={'class':'form-control','placeholder':'Enter about content','size':50}),
   'servicecontent': forms.Textarea(attrs={'class':'form-control','placeholder':'Enter service content','size':50}),
   'solution': forms.Textarea(attrs={'class':'form-control','placeholder':'Enter solution content','size':50}),
   'succestory1': forms.Textarea(attrs={'class':'form-control','placeholder':'Enter success story','size':50}),
   'succestory2': forms.Textarea(attrs={'class':'form-control','placeholder':'Enter success story','size':50}),
   
   }

class ReferralForm(forms.ModelForm):
 class Meta:
  model = referral
  fields = ['Image1', 'Image2', 'Image3','aboutimage1','aboutimage2','aboutimage3','aboutimage4','aboutimage5','aboutimage6','aboutimage7','aboutcontent','servicecontent','solution','succestory1','succestory2','successimage1','successimage2','contact']
  widgets = {
   'aboutcontent': forms.Textarea(attrs={'class':'form-control','placeholder':'Enter about content','size':50}),
   'servicecontent': forms.Textarea(attrs={'class':'form-control','placeholder':'Enter service content','size':50}),
   'solution': forms.Textarea(attrs={'class':'form-control','placeholder':'Enter solution content','size':50}),
   'succestory1': forms.Textarea(attrs={'class':'form-control','placeholder':'Enter success story','size':50}),
   'succestory2': forms.Textarea(attrs={'class':'form-control','placeholder':'Enter success story','size':50}),
   
   }



class EnquiryForm(forms.ModelForm):
 class Meta:
  model = enquiry
  fields = ['name','mobile','email','message']
  widgets = {
   'name': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your name'}),
   'mobile': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your mobile'}),
   'email': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your email'}),
   'message': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your message'}),
   
   }

class quickqueryForm(forms.ModelForm):
 class Meta:
  model = quickquery
  fields = ['qname','qemail','qmessage']
  widgets = {
   'qname': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your name'}),
   'qemail': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your email'}),
   'qmessage': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your message'}),
   
   }


