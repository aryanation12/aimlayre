from django.contrib import admin
from .models import Student, business, referral, quickquery, enquiry
# Register your models here.
@admin.register(Student)
class studentadmin(admin.ModelAdmin):
 list_display = ['Image1', 'Image1', 'Image1','aboutimage1','aboutimage2','aboutimage3','aboutimage4','aboutimage5','aboutimage6','aboutimage7','aboutcontent','servicecontent','solution','succestory1','succestory2','successimage1','successimage1','contact']

@admin.register(business)
class demoadmin(admin.ModelAdmin):
 list_display = ['Image1', 'Image1', 'Image1','aboutimage1','aboutimage2','aboutimage3','aboutimage4','aboutimage5','aboutimage6','aboutimage7','aboutcontent','servicecontent','solution','succestory1','succestory2','successimage1','successimage1','contact']

@admin.register(referral)
class referraladmin(admin.ModelAdmin):
 list_display = ['Image1', 'Image1', 'Image1','aboutimage1','aboutimage2','aboutimage3','aboutimage4','aboutimage5','aboutimage6','aboutimage7','aboutcontent','servicecontent','solution','succestory1','succestory2','successimage1','successimage1','contact']

@admin.register(quickquery)
class quickadmin(admin.ModelAdmin):
 list_display = ['qname','qemail','qmessage']


@admin.register(enquiry)
class quickadmin(admin.ModelAdmin):
 list_display = ['name','mobile','email','message']
