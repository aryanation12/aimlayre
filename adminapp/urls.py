from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

 path('admin/', views.Admin.as_view(), name='dashboard'),
 path('quick/', views.Quickadmin.as_view(), name='quick'),
 path('Enqiryupdate/<int:pk>', views.Enquiry.as_view(), name='updatequery'),
 path('EnquiryDelete/<int:pk>', views.DelEnquiry.as_view(), name='deletequery'),
 path('updatequick/<int:pk>', views.Updatequick.as_view(), name='updatequick'),
 path('updatestud/<int:pk>', views.studentupdate.as_view(), name='updatestud'),
 path('deletestud/<int:pk>', views.Studentdelete.as_view(), name='deletestud'),
 path('stud/', views.Studentview.as_view(), name='stud'),
 path('ref/', views.referralview.as_view(), name='ref'),
 path('quickDelete/<int:pk>', views.Delquick.as_view(), name='deletequick'),
 path('deleteref/<int:pk>', views.Refferaldelete.as_view(), name='deleteref'),
 path('updateref/<int:pk>', views.Refferalupdate.as_view(), name='updateref'),
 path('business/', views.businessview.as_view(), name='busi'),
 path('businessdelete/<int:pk>', views.Businessdelete.as_view(), name='busidel'),
 path('businessupdate/<int:pk>', views.Businessupdate.as_view(), name='busiup'),
 path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html'), name='reset_password'),
 path('homepost/', views.Homepost.as_view(), name='hp'),
 path('businesspost/', views.Businesspost.as_view(), name='bp'),
 path('refferalpost/', views.Refferalpost.as_view(), name='rp'),

]
