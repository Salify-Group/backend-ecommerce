from django.contrib.auth import authenticate

from .models import CustomUserModel

from rest_framework import serializers

import re


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUserModel
        fields = ("id", "email", "username", "first_name", "last_name", "phone")


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUserModel
        fields = ("id", "email", "username", "first_name", "last_name", "phone", "password")

    def validate(self, attrs):
        # username validator
        username = attrs.get("username")
        if not re.match(r'^[a-zA-Z][A-Za-z0-9_.-]+$', username):
            raise serializers.ValidationError(detail={
                "username": "نام کاربری میتواند فقط شامل حروف انگلیسی، اعداد و ( . - _ ) باشد! "
            })
        elif len(username) <= 3 or len(username) > 32:
            raise serializers.ValidationError(detail={
                "username": "نام کاربری حداقل باید شامل 3 حرف و حداکثر شامل 32 حرف باشد"
            })

        # phone validator
        phone = attrs.get("phone")
        if phone == "" or len(phone) == 11:
            pass
        else:
            raise serializers.ValidationError(detail={
                "phone": " شماره تماس نامعتبر است"
            })

        # password validator
        password = attrs.get("password")
        if len(password) < 8 or len(password) > 20:
            raise serializers.ValidationError(detail={
                "password": "!رمز عبور باید بیشتر از 8 رقم باشد"
            })

        return attrs

    def create(self, validated_data):
        password = validated_data.pop("password")

        return CustomUserModel.objects.create_user(password=password, **validated_data)


class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        user = authenticate(**attrs)
        if user and user.is_active:
            return user
        else:
            if not CustomUserModel.objects.filter(email=attrs["email"]).exists():
                raise serializers.ValidationError("کاربری با این ایمیل وجود ندارد! لطفا ثبت نام کنید")
            raise serializers.ValidationError("رمز عبور اشتباه است!!!")

