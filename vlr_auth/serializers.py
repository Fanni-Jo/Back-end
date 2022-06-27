from attr import field
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Worker

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username','email','date_joined')
class UserDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username','email')  

class workerDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Worker
        fields = "__all__"

class workerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Worker
        fields = "__all__"

        