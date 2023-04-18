from django.contrib.auth import get_user_model
from rest_framework import status, views
from rest_framework.generics import GenericAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import (
    CustomerUserSerializer,
    UserListSerializer,
    UserRegistrationSerializer,
    UserLoginSerializer,
)

User = get_user_model()


class UserRegistrationAPIView(GenericAPIView):
    """
    An endpoint for the client to create a new user.
    """

    permission_classes = AllowAny
    serializer_class = UserRegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = RefreshToken.for_user(user)
        data = serializer.data
        data["tokens"] = {"refresh": str(token), "access": str(token.access_token)}
        return Response(data, status=status.HTTP_201_CREATED)


class UserLoginAPIView(GenericAPIView):
    """
    An endpoint to authenticate existing users using their email and password.
    """

    permission_classes = AllowAny
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        serializer = CustomerUserSerializer(user)
        token = RefreshToken.for_user(user)
        data = serializer.data
        data["tokens"] = {"refresh": str(token), "access": str(token.access_token)}
        return Response(data, status=status.HTTP_200_OK)


class UserLogoutAPIView(GenericAPIView):
    """
    An endpoint to logout user.
    """

    permission_classes = IsAuthenticated

    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class UserAPIView(RetrieveUpdateAPIView):
    """
    An endpoint to get and update user information.
    """

    permission_classes = IsAuthenticated
    serializer_class = CustomerUserSerializer

    def get_object(self):
        return self.request.user


class UserListAPIView(views.APIView):
    """
    An endpoint to get users information.
    """

    permission_classes = IsAuthenticated

    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        serializer = UserListSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
