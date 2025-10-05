"""
User-related serializers.
Add these to snippets/serializers.py or create a separate users/serializers.py
"""
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
        style={'input_type': 'password'}
    )

    email = serializers.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
    
    def validate(self, attrs):
        if User.objects.filter(email=attrs['email']).exists():
            raise serializers.ValidationError({
                "email": "A user with this email already exists."
            })
        
        if User.objects.filter(username=attrs['username']).exists():
            raise serializers.ValidationError({
                "username": "A user with this username already exists."
            })
        
        return attrs
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data.get('username'),
            email=validated_data.get('email'),
            password=validated_data.get('password'),
        )
        return user


class UserSerializer(serializers.ModelSerializer):
    snippet_count = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'date_joined',
            'snippet_count'
        ]
        read_only_fields = ['id', 'username', 'date_joined', 'snippet_count']
    
    def get_snippet_count(self, obj):
        """Get total number of snippets for the user."""
        return obj.snippets.count()
