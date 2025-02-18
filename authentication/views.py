from django.shortcuts import render
from rest_framework import generics
from .serilalizers import UserLoginSerializer, UserRegistrationSerializer
from rest_framework.response import Response
from rest_framework import status
from .token import access_token, refresh_token
from django.contrib.auth import get_user_model
from .renderers import UserRenderer


User = get_user_model()


# Create your views here.


class UserLoginView(generics.GenericAPIView):
    serializer_class = UserLoginSerializer
    http_method_names = ["post"]
    renderer_classes = [UserRenderer]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)

        user = User.objects.get(email=serializer.data["email"])

        data = {
            "user": {"email": user.email},
            "access_token": access_token(user.id),
            "refresh_token": refresh_token(user.id),
        }

        return Response(data, status=status.HTTP_200_OK)


class UserRegisterView(generics.GenericAPIView):
    serializer_class = UserRegistrationSerializer
    renderer_classes = [UserRenderer]
    http_method_names = [
        "post",
    ]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
