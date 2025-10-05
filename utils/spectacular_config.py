def get_spectacular_settings():
    base_settings = {
        "TITLE": "SnipBox API",
        "DESCRIPTION": """""",
        "VERSION": "v1",
        "SERVE_INCLUDE_SCHEMA": False,
        "CONTACT": {
            "email": "",
        },
        "ENUM_NAME_OVERRIDES": {"status": "MyCustomStatusEnum"},
        "SCHEMA_PATH_PREFIX": "/api/",
        "COMPONENT_SPLIT_REQUEST": True,
        "SWAGGER_UI_SETTINGS": {
            "deepLinking": True,
            "persistAuthorization": True,
            "displayOperationId": True,
        },
        "SERVE_PERMISSIONS": ["rest_framework.permissions.AllowAny"],
        "AUTHENTICATION_WHITELIST": [
            "rest_framework_simplejwt.authentication.JWTAuthentication",
            "utils.custom_authentication.CustomJWTAuthentication",
        ],
    }

    return base_settings
