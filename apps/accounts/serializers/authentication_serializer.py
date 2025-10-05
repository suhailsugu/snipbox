from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken



class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(
        required=True,
        write_only=True,
        style={'input_type': 'password'}
    )
    
    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        user = authenticate(
            username=username,
            password=password
        )
        
        if user is None:
            raise serializers.ValidationError(
                'Invalid credentials. Please try again.'
            )
        
        if not user.is_active:
            raise serializers.ValidationError(
                'User account is disabled.'
            )
        
        attrs['user'] = user
        return attrs
    


class LoginResponseSchema(serializers.ModelSerializer):
    username    = serializers.CharField(allow_null=True)
    email       = serializers.EmailField(allow_null=True)
    tokens      = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id','username','email','tokens']

    def get_tokens(self,instance):
        refresh = RefreshToken.for_user(instance)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)
        data=  {
            'access': access_token,
            'refresh': refresh_token,
            'token_type': 'Bearer'
        }
        return data


    def to_representation(self, instance):
        datas = super().to_representation(instance)
        for key in datas.keys():
            try:
                if datas[key] is None:
                    datas[key] = ""
            except KeyError:
                pass
        return datas


class RefreshTokenSerializer(serializers.Serializer):
    refresh = serializers.CharField(required=True)
    
    def validate(self, attrs):
        refresh_token = attrs.get('refresh')
        
        try:
            refresh = RefreshToken(refresh_token)
            attrs['access'] = str(refresh.access_token)
        except Exception as e:
            raise serializers.ValidationError(
                'Invalid or expired refresh token.'
            )
        
        return attrs


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField(required=True)
    
    def validate(self, attrs):
        self.token = attrs.get('refresh')
        return attrs
    
    def save(self, **kwargs):
        try:
            token = RefreshToken(self.token)
            token.blacklist()
        except Exception:
            raise serializers.ValidationError(
                'Invalid or expired token.'
            )