from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serilaizers import SignupSerializer, LoginSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class SignupAPIView(APIView):
    """
    회원가입 API
    
    - username, password, nickname을 입력받아 회원가입을 진행합니다.
    - username과 nickname은 고유해야 하며, 이미 존재하는 경우 에러를 반환합니다.
    - 회원가입 성공 시, username과 nickname을 포함한 응답을 반환합니다.
    """

    @swagger_auto_schema(
        request_body=SignupSerializer,
        responses={
            201: openapi.Response(
                description="회원가입 성공",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "username": openapi.Schema(type=openapi.TYPE_STRING),
                        "nickname": openapi.Schema(type=openapi.TYPE_STRING),
                    },
                    example={
                        "username": "JIN HO",
                        "nickname": "Mentos"
                    }
                )
            ),
            400: openapi.Response(
                description="회원가입 실패",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "error": openapi.Schema(
                            type=openapi.TYPE_OBJECT,
                            properties={
                                "code": openapi.Schema(type=openapi.TYPE_STRING),
                                "message": openapi.Schema(type=openapi.TYPE_STRING),
                            }
                        )
                    },
                    example={
                        "error": {
                            "code": "USER_ALREADY_EXISTS",
                            "message": "이미 가입된 사용자입니다."
                        }
                    }
                )
            )
        }
    )
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                "username": user.username,
                "nickname": user.nickname
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(APIView):
    """
    로그인 API

    - username과 password를 입력받아 토큰을 발급합니다.
    - 아이디/비밀번호가 올바르지 않으면 에러를 반환합니다.
    """

    @swagger_auto_schema(
        request_body=LoginSerializer,
        responses={
            200: openapi.Response(
                description="로그인 성공",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "token": openapi.Schema(type=openapi.TYPE_STRING)
                    },
                    example={
                        "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
                    }
                )
            ),
            400: openapi.Response(
                description="로그인 실패",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "error": openapi.Schema(
                            type=openapi.TYPE_OBJECT,
                            properties={
                                "code": openapi.Schema(type=openapi.TYPE_STRING),
                                "message": openapi.Schema(type=openapi.TYPE_STRING),
                            }
                        )
                    },
                    example={
                        "error": {
                            "code": "INVALID_CREDENTIALS",
                            "message": "아이디 또는 비밀번호가 올바르지 않습니다."
                        }
                    }
                )
            )
        }
)

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
