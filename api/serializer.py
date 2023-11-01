from django.contrib.auth.password_validation import validate_password
from django.core import exceptions
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
User = get_user_model()

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token['name'] = user.name
        token['email'] = user.email
        token['phonenumber'] = user.phonenumber
        token['id'] = user.id
        
        token['image'] = "http://127.0.0.1:8000/api/users"+user.image.url if user.image else 'https://bootdey.com/img/Content/avatar/avatar7.png'
        return token
   
   
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "name",
            "phonenumber",
            "email","image"
        )
