from rest_framework import serializers, exceptions
from django.contrib.auth import authenticate

from django.contrib.auth import get_user_model

User = get_user_model()


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(
        write_only=True,
    )

    def validate(self, data):
        request = self.context.get("request")
        email = data.get("email")
        password = data.get("password")

        print(email, password)

        if not email:
            raise exceptions.ValidationError("email must be provided.")

        try:
            user = User.objects.get(email=email)

        except User.DoesNotExist:
            raise serializers.ValidationError("user with that email does not exist.")

        if not user.check_password(password):
            raise serializers.ValidationError("Invalid email or password.")

        return data


class UserRegistrationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get("email")
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError("user with that email already exists")

        return data

    def create(self, validated_data):
        user = User(email=validated_data["email"])
        user.set_password(validated_data["password"])
        user.save()
        return user
