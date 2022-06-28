from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
   is_customer =models.BooleanField(default=False)
   is_worker =models.BooleanField(default=False)
   first_name = models.CharField(max_length=100)
   last_name = models.CharField(max_length=100)



class Customer (models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    phone_number  =models.CharField(max_length=20)
    location =models.CharField(max_length=20)


class Worker(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    phone_number  =models.CharField(max_length=20)
    location =models.CharField(max_length=20)
    designation =models.CharField(max_length=20)
    years_of_exp = models.IntegerField(verbose_name='experience')
    image = models.FileField(null=True, blank=True, verbose_name='image')



    def __str__(self):
        return self.username
