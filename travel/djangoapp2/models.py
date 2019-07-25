from django.db import models

# Create your models here.
class booking(models.Model):
    fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=30)
    email=models.EmailField(max_length=50)
    place=models.CharField(max_length=30)
    date_of_journey=models.DateField()
    contact_no=models.CharField(max_length=10)
