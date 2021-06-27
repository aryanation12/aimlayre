from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home.as_view(), name='home'),
    path('business/',views.business.as_view(), name='business'),
    path('referral/',views.referral.as_view(), name='referral'),
    path('',views.pop.as_view(), name='pop'),
]
