from django.db import models

# Create your models here.
class Person(models.Model):
    Gender =[('female','FEMALE'),('male','MALE')]
    pid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=23)
    city = models.CharField(max_length=23)
    gender = models.CharField(max_length=23,choices=Gender)
    profile_pic = models.ImageField(upload_to='Profile')