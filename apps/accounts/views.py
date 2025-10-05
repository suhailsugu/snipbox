from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema
from apps.accounts.serializers.user_serializer import (
    UserRegistrationSerializer,
)
from apps.accounts.serializers.authentication_serializer import (
    LoginSerializer,
    RefreshTokenSerializer,
    LogoutSerializer,
    LoginResponseSchema
)


class UserRegistrationAPIView(APIView):
    permission_classes = [AllowAny]

    @extend_schema(
        tags=["Accounts"],
        operation_id="user-registration",
        request=UserRegistrationSerializer,
        description="This endpoint allows new users to register by providing a username, email, and password. Upon successful registration, it returns the user's details along with JWT access and refresh tokens.",
    )
    def post(self, request):
        try:
            serializer = UserRegistrationSerializer(data=request.data,context={'request': request})
            if not serializer.is_valid():
                return Response(
                    {
                        "message": serializer.errors,
                        "status": False,
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
         
            user = serializer.save()
            data = LoginResponseSchema(user, context={'request': request}).data
            return Response(
                {
                    "message": "User registration successfull",
                    "status": True,
                    "data": data
                },
                status=status.HTTP_200_OK,
            )
        
        except Exception as e:
            return Response(
                {
                    "message": "An unexpected error occurred. Please try again later.",
                    "status": False,
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class LoginAPIView(APIView):
    permission_classes = [AllowAny]

    @extend_schema(
        tags=["Accounts"],
        operation_id="login",
        request=LoginSerializer,
        description="This endpoint allows users to log in by providing their username and password. Upon successful authentication, it returns user details along with JWT access and refresh tokens.",
    )
    def post(self, request):
        try:
            serializer = LoginSerializer(data=request.data)
            if not serializer.is_valid():
                return Response(
                    {
                        "message": serializer.errors,
                        "status": False,
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
         
            user = serializer.validated_data.get('user')
            data = LoginResponseSchema(user, context={'request': request}).data
            return Response(
                {
                    "message": "Login successfull",
                    "status": True,
                    "data": data
                },
                status=status.HTTP_200_OK,
            )
        
        except Exception as e:
            return Response(
                {
                    "message": "An unexpected error occurred. Please try again later.",
                    "status": False,
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class RefreshTokenAPIView(APIView):
    permission_classes = [AllowAny]

    @extend_schema(
        tags=["Accounts"],
        operation_id="refresh_token",
        request=RefreshTokenSerializer,
        description="This endpoint allows users to refresh their JWT access token using a valid refresh token. It returns a new access token if the provided refresh token is valid.",
    )
    def post(self, request):
        try:
            serializer = RefreshTokenSerializer(data=request.data)
            if not serializer.is_valid():
                return Response(
                    {
                        "message": serializer.errors,
                        "status": False,
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
         
            return Response({
                'success': True,
                'message': 'Token refreshed successfully',
                'access': serializer.validated_data['access']
            }, status=status.HTTP_200_OK)
        
        except Exception as e:
            print("<<<<<<<<<<<<<",str(e))
            return Response(
                {
                    "message": "An unexpected error occurred. Please try again later.",
                    "status": False,
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        tags=["Accounts"],
        operation_id="logout",
        request=LogoutSerializer,
        description="This endpoint allows users to log out by blacklisting their refresh token, preventing further use of that token for obtaining new access tokens.",
    )
    def post(self, request):
        try:
            serializer = LogoutSerializer(data=request.data)
            if not serializer.is_valid():
                return Response(
                    {
                        "message": serializer.errors,
                        "status": False,
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
         
            serializer.save()
            return Response({
                'success': True,
                'message': 'Logout successful'
            }, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response(
                {
                    "message": "An unexpected error occurred. Please try again later.",
                    "status": False,
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
   