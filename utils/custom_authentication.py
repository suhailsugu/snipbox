from drf_spectacular.extensions import OpenApiAuthenticationExtension
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError


class CustomJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        try:
            result = super().authenticate(request)
            if result is None:
                return None

            user, validated_token = result

            if hasattr(user, "sso_superadmin"):
                try:
                    sso_instance = user.sso_superadmin.get()
                    if not sso_instance:
                        return None
                except Exception:
                    return None

            return user, validated_token

        except (InvalidToken, TokenError):
            return None


class CustomJWTAuthenticationScheme(OpenApiAuthenticationExtension):
    target_class = CustomJWTAuthentication
    name = "CustomJWTAuth"

    priority = 0

    def get_security_definition(self, auto_schema):
        return {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT",
            "description": "JWT token authentication with SSO superadmin validation",
        }

    def get_security_requirement(self, auto_schema):
        return {self.name: []}
