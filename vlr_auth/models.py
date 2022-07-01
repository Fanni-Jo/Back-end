from django.core.validators import MaxValueValidator , MinValueValidator
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models

# class NewUserProfile(AbstractUser):

#     phone_number =PhoneNumberField(null=False, blank=False, unique=True,region="JO",help_text="Please start with +962")
#     image = models.ImageField(blank=True,null=True)
#     # address = models.CharField(max_length=12,choices =cities)
#     def __str__(self):
#         return self.name
    
class Category(models.Model):
    title = models.CharField(verbose_name='Category',max_length=1000)
    # parent = TreeForeignKey(
    #     "self", on_delete=models.CASCADE, null=True, blank=True, related_name="children"
    # )
    def __str__(self):
        return str(self.title)
    
    class Meta:
        verbose_name_plural = ('Categories')
        verbose_name = ('Category')


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
class ServiceProviderProfile(models.Model):
    
    
    username = models.OneToOneField(User, on_delete=models.CASCADE)

    category = models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name='Category ')
    phone = PhoneNumberField(verbose_name='phone no.',unique=True)
    phone2 = PhoneNumberField(null=True, blank=True,verbose_name='secondary phone no.')
    email = models.EmailField(verbose_name='email',blank=True,null=True)
    address = models.TextField(verbose_name='address')
    years_of_exp = models.IntegerField(verbose_name='experience')
    profile_picture=models.ImageField(upload_to='profile-pictures-service-providers/',blank=True)

    media = models.FileField(upload_to='profile_pictures/',null=True, blank=True, verbose_name='image')
    date = models.DateTimeField(auto_now_add=True,editable=False)
    gender= models.CharField(max_length=6,choices=[('MALE','MALE'),('FEMALE','FEMALE')],default=None)
   
    def get_absolute_url(self):
        return f'/service_provider/{self.username}'
    def __str__(self):
        return str(self.username)

    def save(self, *args, **kwargs):
        self.username = self.username
        super(ServiceProviderProfile, self).save(*args, **kwargs)
        
    class Meta:
    
        ordering = ('-date',)
        verbose_name_plural = ('service providers')
        verbose_name = ('service provider')
            
class Profile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = PhoneNumberField(null=False, blank=False, unique=True,region='JO')
    profile_picture=models.ImageField(upload_to='profile_pictures/',blank=True)
    birthdate=models.DateField(null=True, blank=True)
    gender= models.CharField(max_length=6,choices=[('MALE','MALE'),('FEMALE','FEMALE')],default=None,blank=True,null=True)
    
    # def save(self,*args,**kwargs):
    #     return super().save(*args,**kwargs)
    
    def __str__(self):
        return self.username
    
class Review(models.Model):
    username=models.ForeignKey(User ,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)
    text=models.TextField(max_length=3000 ,blank =True)
    stars=models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])

    # class Meta:
    #     unique_together =
    def save(self, *args, **kwargs):
        self.username = get_user_model().objects.get(id=self.username.id)
        super(Review, self).save(*args, **kwargs)
    def __str__(self):
        return self.username

class ReviewWorkerRating(models.Model):
    # ondelete cascade if the worker delete the comment will also delete
    # added_by_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, default= None)
    # models.CharField(max_length=100,default=None,help_text="servicer_provider")
#   models.ForeignKey(ServicerProviderProfile,on_delete=models.CASCADE)        
    service_provider=models.ForeignKey(ServiceProviderProfile,on_delete=models.CASCADE)   
    username=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    # username=models.ForeignKey(User.get_full_name,on_delete=models.CASCADE)
    subject=models.CharField(max_length=100,blank=True)
    review=models.TextField(max_length=500,blank=True)
    # rating=models.FloatField()
    #choice field 
    rating=models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    #for admin if he want to diable a comment
    status=models.BooleanField(default=True)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject