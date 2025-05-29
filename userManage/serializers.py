from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken


class RegisterSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):

        if User.objects.filter(username=data['username']).exists():
            raise serializers.ValidationError("Username already taken.")
        
        elif User.objects.filter(email=data['email']).exists():
            raise serializers.ValidationError("Email already taken.")
        
        return data
        
    def create(self, validated_data):
        user = User.objects.create(
            first_name=validated_data['first_name'], 
            last_name=validated_data['last_name'], 
            username=validated_data['username'], 
            email=validated_data['email']
            )
        user.set_password(validated_data['password'])
        user.save()
        return validated_data
    
class LoginSerializer(serializers.Serializer):

    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):

        if not User.objects.filter(username=data['username']).exists():
            raise serializers.ValidationError("Username dosen't exists.")

        user = authenticate(username=data['username'], password=data['password'])
        if not user:
            raise serializers.ValidationError("Invalid username or password.")
        
        data['user'] = user  # Save user for use in get_jwt_token
        return data

    def get_jwt_token(self,validated_data):

        user = validated_data['user']
        refresh = RefreshToken.for_user(user)

        return {"message": "Login success.", "data":{'token': {'refresh': str(refresh),
        'access': str(refresh.access_token)}}}
