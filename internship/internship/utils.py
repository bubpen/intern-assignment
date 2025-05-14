from rest_framework.views import exception_handler
from rest_framework.exceptions import NotAuthenticated
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework.response import Response
from rest_framework import status

def custom_exception_handler(exc, context):
    if isinstance(exc, InvalidToken):
        return Response({
            "error": {
                "code": "INVALID_TOKEN",
                "message": "토큰이 유효하지 않습니다."
            }
        }, status=status.HTTP_401_UNAUTHORIZED)

    elif isinstance(exc, TokenError) and "expired" in str(exc).lower():
        return Response({
            "error": {
                "code": "TOKEN_EXPIRED",
                "message": "토큰이 만료되었습니다."
            }
        }, status=status.HTTP_401_UNAUTHORIZED)

    elif isinstance(exc, NotAuthenticated):
        return Response({
            "error": {
                "code": "TOKEN_NOT_FOUND",
                "message": "토큰이 없습니다."
            }
        }, status=status.HTTP_401_UNAUTHORIZED)

    return exception_handler(exc, context)
