from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Departments(models.Model):
    dep_name = models.CharField(max_length=100)
    dep_description = models.TextField()
    dep_image = models.ImageField(upload_to='department')

    def __str__(self):
        return self.dep_name

class Doctors(models.Model):
    doc_name = models.CharField(max_length=255)
    doc_spec = models.CharField(max_length=255)
    dep_name = models.ForeignKey(Departments, on_delete=models.CASCADE)
    doc_image = models.ImageField(upload_to='doctors')

    def __str__(self):
        return 'Dr.' + self.doc_name + ' - (' + self.doc_spec + ')'

class Booking(models.Model):
    p_name = models.CharField(max_length=255)
    p_phone = models.CharField(max_length=10)
    p_email = models.EmailField()
    doc_name = models.ForeignKey(Doctors, on_delete= models.CASCADE)
    Booking_date = models.DateField()
    Booked_on = models.DateField(auto_now=True)

class CustumUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(default='default/user.jpg', upload_to='profile_picture')