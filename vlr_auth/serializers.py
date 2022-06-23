from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'username','email','phone_number' )
        
