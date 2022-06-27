from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
# from mptt.models import MPTTModel, TreeForeignKey

# class NewUserProfile(AbstractUser):

#     phone_number =PhoneNumberField(null=False, blank=False, unique=True,region="JO",help_text="Please start with +962")
#     image = models.ImageField(blank=True,null=True)
#     # address = models.CharField(max_length=12,choices =cities)
#     def __str__(self):
#         return self.name
    
class Category(models.Model):
    title = models.CharField(verbose_name='service type',max_length=1000)
    # parent = TreeForeignKey(
    #     "self", on_delete=models.CASCADE, null=True, blank=True, related_name="children"
    # )
    def __str__(self):
        return str(self.title)
    # class MPTTMeta:
    #     order_insertion_by = ["title"]

    class Meta:
        verbose_name_plural = ('services')
        verbose_name = ('service')


# for sub categories 
# class Service(models.Model):
#     title = models.CharField(max_length=10000,verbose_name='service title')
    
#     time = models.CharField(max_length=10000,verbose_name='time')
#     price = models.FloatField(verbose_name='service cost')
#     date = models.DateTimeField(default=timezone.now,editable=False)
#     def __str__(self):
#         return str(self.title)

#     class Meta:
#         ordering = ('-date',)
#         verbose_name_plural = ('services')
#         verbose_name = ('service')

class Worker(models.Model):
    
    first_name = models.CharField(verbose_name='worker first name', max_length=10000, unique=True)
    last_name = models.CharField(verbose_name='worker last name', max_length=10000, unique=True)
    username=models.CharField(verbose_name='username', max_length=10000, unique=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name='service type')
    phone = PhoneNumberField(verbose_name='phone no.',unique=True)
    phone2 = PhoneNumberField(null=True, blank=True,verbose_name='secondary phone no.')
    email = models.EmailField(verbose_name='email',unique=True)
    address = models.TextField(verbose_name='address')
    years_of_exp = models.IntegerField(verbose_name='experience')
    media = models.FileField(null=True, blank=True, verbose_name='image')
    date = models.DateTimeField(default=timezone.now,editable=False)
    # password=models.CharField()
    def get_absolute_url(self):
        return f'/worker/{self.username}'
    def __str__(self):
        return str(self.username)

    class Meta:
        ordering = ('-date',)
        verbose_name_plural = ('workers')
        verbose_name = ('worker')

# class Client(models.Model):
#     name = models.CharField(verbose_name='اسم العميل',max_length=10000,unique=True)
#     phone = PhoneNumberField(verbose_name='رقم الهاتف')
#     email = models.EmailField(verbose_name='البريد الالكتروني')
#     address = models.TextField(verbose_name='العنوان')
#     content = models.TextField(null=True,blank=True,verbose_name=' ملاحظات')
#     media = models.FileField(null=True,blank=True,verbose_name='ملفات ميديا')
#     date = models.DateTimeField(default=timezone.now,editable=False)
#     def get_absolute_url(self):
#         return f'/client/{self.id}'

#     def __str__(self):
#         return str(self.name)

#     class Meta:
#         ordering = ('-date',)
#         verbose_name_plural = ('العملاء')
#         verbose_name = ('عميل')

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = PhoneNumberField(null=False, blank=False, unique=True,region='JO')
    profile_picture=models.ImageField(upload_to='profile_pictures/',blank=True)
    birthdate=models.DateField(null=True, blank=True)
    # gender= models.CharField(max_length=6,choices=[('MALE','MALE'),('FEMALE','FEMALE')],default="MALE")
    
    def __str__(self):
        return self.user.username