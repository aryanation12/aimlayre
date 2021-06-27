from django.db import models
import cloudinary
from cloudinary.models import CloudinaryField
from django.db.models.fields import TextField
from django.urls import reverse

# Create your models here.

class Student(models.Model):
 Image1 =cloudinary.models.CloudinaryField('bannerimage1')
 Image2 =cloudinary.models.CloudinaryField('bannerimage2')
 Image3 =cloudinary.models.CloudinaryField('bannerimage3')
 aboutimage1 =cloudinary.models.CloudinaryField('aboutimage1')
 aboutimage2 =cloudinary.models.CloudinaryField('aboutimage2')
 aboutimage3 =cloudinary.models.CloudinaryField('aboutimage3')
 aboutimage4 =cloudinary.models.CloudinaryField('aboutimage4')
 aboutimage5 =cloudinary.models.CloudinaryField('aboutimage5')
 aboutimage6 =cloudinary.models.CloudinaryField('aboutimage6')
 aboutimage7 =cloudinary.models.CloudinaryField('aboutimage7')
 aboutcontent = models.TextField()
 servicecontent = models.TextField()
 solution = models.TextField()
 succestory1 = models.TextField()
 succestory2 = models.TextField()
 successimage1 =cloudinary.models.CloudinaryField('successimage1')
 successimage2 =cloudinary.models.CloudinaryField('successimage2')
 contact = models.CharField(max_length=50)

 def __str__(self):
        return str(self.id)

class business(models.Model):
 Image1 =cloudinary.models.CloudinaryField('bannerimage1')
 Image2 =cloudinary.models.CloudinaryField('bannerimage2')
 Image3 =cloudinary.models.CloudinaryField('bannerimage3')
 aboutimage1 =cloudinary.models.CloudinaryField('aboutimage1')
 aboutimage2 =cloudinary.models.CloudinaryField('aboutimage2')
 aboutimage3 =cloudinary.models.CloudinaryField('aboutimage3')
 aboutimage4 =cloudinary.models.CloudinaryField('aboutimage4')
 aboutimage5 =cloudinary.models.CloudinaryField('aboutimage5')
 aboutimage6 =cloudinary.models.CloudinaryField('aboutimage6')
 aboutimage7 =cloudinary.models.CloudinaryField('aboutimage7')
 aboutcontent = models.TextField()
 servicecontent = models.TextField()
 solution = models.TextField()
 succestory1 = models.TextField()
 succestory2 = models.TextField()
 successimage1 =cloudinary.models.CloudinaryField('successimage1')
 successimage2 =cloudinary.models.CloudinaryField('successimage2')
 contact = models.CharField(max_length=50)
 def __str__(self):
        return str(self.id)

class referral(models.Model):
 Image1 =cloudinary.models.CloudinaryField('bannerimage1')
 Image2 =cloudinary.models.CloudinaryField('bannerimage2')
 Image3 =cloudinary.models.CloudinaryField('bannerimage3')
 aboutimage1 =cloudinary.models.CloudinaryField('aboutimage1')
 aboutimage2 =cloudinary.models.CloudinaryField('aboutimage2')
 aboutimage3 =cloudinary.models.CloudinaryField('aboutimage3')
 aboutimage4 =cloudinary.models.CloudinaryField('aboutimage4')
 aboutimage5 =cloudinary.models.CloudinaryField('aboutimage5')
 aboutimage6 =cloudinary.models.CloudinaryField('aboutimage6')
 aboutimage7 =cloudinary.models.CloudinaryField('aboutimage7')
 aboutcontent = models.TextField()
 servicecontent = models.TextField()
 solution = models.TextField()
 succestory1 = models.TextField()
 succestory2 = models.TextField()
 successimage1 =cloudinary.models.CloudinaryField('successimage1')
 successimage2 =cloudinary.models.CloudinaryField('successimage2')
 contact = models.CharField(max_length=50)

 def __str__(self):
        return str(self.id)

class quickquery(models.Model):
 qname =models.CharField(max_length=50)
 qemail = models.EmailField(max_length=254)
 qmessage = models.TextField()

class enquiry(models.Model):
 name = models.CharField(max_length=50)
 mobile = models.CharField(max_length=50)
 email = models.EmailField(max_length=254)
 message = models.TextField()
 