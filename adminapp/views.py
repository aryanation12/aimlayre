from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import ListView, UpdateView, DetailView
from django.views.generic.edit import CreateView, DeleteView
from app.models import quickquery, enquiry, Student, referral, business
from django.urls import reverse_lazy
from .forms import StudentForm, BusinessForm, ReferralForm, EnquiryForm, quickqueryForm

#admin start customer detail

class Admin(ListView):
 model = enquiry
 template_name = 'admin.html'

class Enquiry(UpdateView):
 model = enquiry
 form_class = EnquiryForm
 template_name = 'updateshow/updateenq.html'
 def get_success_url(self):
     return reverse_lazy('dashboard')

class DelEnquiry(DeleteView):
 model = enquiry
 template_name = 'deletepost/delstu.html'
 def get_success_url(self):
     return reverse_lazy('dashboard')
    
class Quickadmin(ListView):
 model = quickquery
 template_name = 'quickenq.html'

class Updatequick(UpdateView):
 model = quickquery
 form_class = quickqueryForm
 template_name = 'updateshow/updatequick.html'
 def get_success_url(self):
     return reverse_lazy('dashboard')

class Delquick(DeleteView):
 model = quickquery
 template_name = 'deletepost/delquick.html'
 def get_success_url(self):
     return reverse_lazy('dashboard')

#student 

class Studentview(ListView):
      model = Student
      template_name = 'show/candidate.html'

class Studentdelete(DeleteView):
 model = Student
 template_name = 'deletepost/deletehome.html'
 def get_success_url(self):
      return reverse_lazy('dashboard')

class studentupdate(UpdateView):
 model = Student
 form_class = StudentForm
 template_name = 'updateshow/homeupdate.html'
 def get_success_url(self):
      return reverse_lazy('dashboard')


# #end student

# #referral


class referralview(ListView):
      model = referral
      template_name = 'show/referralAdmin.html'


class Refferaldelete(DeleteView):
 model = referral
 template_name = 'deletepost/deleteReferral.html'
 def get_success_url(self):
      return reverse_lazy('dashboard')

class Refferalupdate(UpdateView):
 model = referral
 form_class = ReferralForm
 template_name = 'updateshow/updateref.html'
 def get_success_url(self):
      return reverse_lazy('dashboard')

class businessview(ListView):
      model = business
      template_name = 'show/businessadmin.html'


class Businessdelete(DeleteView):
 model = business
 template_name = 'deletepost/deletebusiness.html'
 def get_success_url(self):
      return reverse_lazy('dashboard')

class Businessupdate(UpdateView):
 model = business
 form_class = BusinessForm
 template_name = 'updateshow/businessupdate.html'
 def get_success_url(self):
      return reverse_lazy('dashboard')

class Businesspost(CreateView):
 model = business
 form_class = BusinessForm
 template_name = 'post/businesspost.html'
 def get_success_url(self):
      return reverse_lazy('dashboard')
 
class Refferalpost(CreateView):
 model = referral
 form_class = ReferralForm
 template_name = 'post/referrapost.html'
 def get_success_url(self):
      return reverse_lazy('dashboard')
 
class Homepost(CreateView):
 model = Student
 form_class = StudentForm
 template_name = 'post/postindex.html'
 def get_success_url(self):
      return reverse_lazy('dashboard')
 