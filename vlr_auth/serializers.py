from rest_framework import serializers
from django.contrib.auth.models import User
from .models import ServiceProviderProfile,Profile,Review,ReviewWorkerRating

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = '__all__'
        

        
class ServiceProviderProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ServiceProviderProfile
        fields = ('category','phone','phone2','email','address','years_of_exp','media','gender','profile_picture')
        
    
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
        fields = ["service_provider","subject","username","review","rating","created_date","updated_date"]        