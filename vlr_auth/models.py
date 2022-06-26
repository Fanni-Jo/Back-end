from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser

class NewUserProfile(AbstractUser):

    phone_number =PhoneNumberField(null=False, blank=False, unique=True,region="JO",help_text="Please start with +962")
    image = models.ImageField(blank=True,null=True)
    address = models.CharField(max_length=12,choices =cities)
    def __str__(self):
        return self.name
    
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = PhoneNumberField(null=False, blank=False, unique=True,region='JO')
    profile_picture=models.ImageField(upload_to='profile_pictures/',blank=True)
    # birthdate=models.DateField(null=True, blank=True)
    # gender= models.CharField(max_length=6,choices=[('MALE','MALE'),('FEMALE','FEMALE')])
    
    def __str__(self):
        return self.user.username