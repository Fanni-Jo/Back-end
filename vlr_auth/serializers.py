from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from .models import ServiceProviderProfile,Profile,Review,ReviewWorkerRating,Category

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = '__all__'
        

        
class ServiceProviderProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ServiceProviderProfile
        fields = ('username','category','first_name','last_name','phone','phone2','email','address','years_of_exp','media','gender','profile_picture')
    # def save(self): 
    #     category= Category.objects.get(title=self.Meta.model.category)
        
    
class ClientSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Profile
        fields = "__all__"
        

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model=Review
        fields =('id' ,'stars','username','date','text')
                      
   

class ReviewServiceProviderSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = ReviewWorkerRating
        fields = ["service_provider","subject","username","first_name","last_name","review","rating","created_date","updated_date"]
    def save(self,*args,**kwargs):
        self.username = get_user_model().objects.get(id=self.username.id)  
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"                  