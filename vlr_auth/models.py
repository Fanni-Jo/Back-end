from django.core.validators import MaxValueValidator , MinValueValidator
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    title = models.CharField(verbose_name='Category',max_length=1000)
   
    def __str__(self):
        return str(self.title)
    
    class Meta:
        verbose_name_plural = ('Categories')
        verbose_name = ('Category')

def upload_path(instance, filname):
    return '/'.join(['covers', str(instance.username), filname])
def upload_path_media(instance, filname):
    return '/'.join(['covers', str(instance.username), filname])

class ServiceProviderProfile(models.Model):
    
    
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name= models.CharField(verbose_name='first_name',max_length=100,null=True,blank=True)
    last_name= models.CharField(verbose_name='last_name',max_length=100,null=True,blank=True)

    category = models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name='Category ')
    phone = PhoneNumberField(verbose_name='phone no.',unique=True)
    phone2 = PhoneNumberField(null=True, blank=True,verbose_name='secondary phone no.')
    email = models.EmailField(verbose_name='email',blank=True,null=True)
    address = models.TextField(verbose_name='address')
    years_of_exp = models.IntegerField(verbose_name='experience')
    profile_picture=models.ImageField(upload_to=upload_path,blank=True,null=True,verbose_name='profile picture')
    
    media = models.FileField(upload_to=upload_path_media,null=True, blank=True, verbose_name='image')
    date = models.DateTimeField(auto_now_add=True,editable=False)
    gender= models.CharField(max_length=6,choices=[('MALE','MALE'),('FEMALE','FEMALE')],default=None)
   
    def get_absolute_url(self):
        return f'/service_provider/{self.username}'
      
    class Meta:
    
        ordering = ('-date',)
        verbose_name_plural = ('service providers')
        verbose_name = ('service provider')
            
class Profile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = PhoneNumberField(null=False, blank=False, unique=True,region='JO')
    profile_picture=models.ImageField(upload_to=upload_path,blank=True,null=True)
    birthdate=models.DateField(null=True, blank=True)
    gender= models.CharField(max_length=6,choices=[('MALE','MALE'),('FEMALE','FEMALE')],default=None,blank=True,null=True)
    
    # def save(self,*args,**kwargs):
    #     return super().save(*args,**kwargs)
    
    # def __str__(self):
    #     return self.username
    
class Review(models.Model):
    username=models.ForeignKey(User ,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)
    text=models.TextField(max_length=3000 ,blank =True)
    stars=models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    class Meta:
        ordering = ('-date',)
        verbose_name_plural = ('reviews')
        verbose_name = ('review')
        
    def save(self, *args, **kwargs):
        self.username = get_user_model().objects.get(id=self.username.id)
        return super(Review, self).save(*args, **kwargs)
   

class ReviewWorkerRating(models.Model):
    # ondelete cascade if the worker delete the comment will also delete
    # added_by_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, default= None)
    # models.CharField(max_length=100,default=None,help_text="servicer_provider")
#   models.ForeignKey(ServicerProviderProfile,on_delete=models.CASCADE)        
    service_provider=models.CharField(max_length=100,default=None,help_text="servicer_provider")  
    username=models.CharField(max_length=100,default=None,help_text="username")
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