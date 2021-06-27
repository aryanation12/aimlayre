from django.db.models import query
from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
from django.views import View
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from .models import Student, quickquery, enquiry, referral, business
from .forms import quickqueryForm

class pop(TemplateView):
   template_name = 'home.html'


class home(ListView):
   model = Student
   template_name = 'index.html'

   def post(self, request):
      if request.method == 'POST':
         if 'dbutton' in request.POST:
            nm = request.POST['sname']
            em = request.POST['semail']
            ms = request.POST['smsg']
            x = quickquery(qname=nm, qemail=em, qmessage=ms)
            x.save()
         elif 'ubutton' in request.POST:
            name = request.POST['stuname']
            mobile = request.POST['stucontact']
            email = request.POST['stumail']
            msg = request.POST['msg']
            x = enquiry(name=name, email=email,mobile=mobile ,message=msg)
            x.save()
      return render(request, 'index.html')

class business(ListView):
   model = business
   template_name = 'business_partner.html'


   def post(self, request):
      if request.method == 'POST':
         if 'dbutton' in request.POST:
            nm = request.POST['bname']
            em = request.POST['bemail']
            ms = request.POST['bmsg']
            x = quickquery(qname=nm, qemail=em, qmessage=ms)
            x.save()
         elif 'ubutton' in request.POST:
            name = request.POST['businame']
            mobile = request.POST['busicontact']
            email = request.POST['busimail']
            msg = request.POST['busimsg']
            x = enquiry(name=name, email=email,mobile=mobile ,message=msg)
            x.save()
      return render(request, 'business_partner.html')

 


class referral(ListView):
   model = referral
   template_name = 'referral.html'

   def post(self, request):
      if request.method == 'POST':
         if 'dbutton' in request.POST:
            nm = request.POST['rname']
            em = request.POST['remail']
            ms = request.POST['rmsg']
            x = quickquery(qname=nm, qemail=em, qmessage=ms)
            x.save()
         elif 'ubutton' in request.POST:
            name = request.POST['refname']
            mobile = request.POST['refcontact']
            email = request.POST['refmail']
            msg = request.POST['refmsg']
            x = enquiry(name=name, email=email,mobile=mobile ,message=msg)
            x.save()
      return render(request, 'business_partner.html')

