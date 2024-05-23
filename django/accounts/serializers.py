from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    profile_pic = serializers.ImageField(source='profile.profile_pic')
    
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'profile_pic']

class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['pk', 'username', 'email', 'profile_pic']
        read_only_fields = ['email', 'profile_pic']
