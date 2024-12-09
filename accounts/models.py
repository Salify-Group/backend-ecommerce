import re

from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser


def validate_email(email):
    if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
        raise ValidationError(message="فرمت ایمیل خود را اصلاح کنید")
    elif email == "" or email == None:
        raise ValidationError(message="ایمیل نمیتواند خالی باشد")


class CustomUserModel(AbstractUser):
    username = models.CharField(max_length=32, unique=True, blank=False, null=False, error_messages={
        "unique": "این نام کاربری قبلا استفاده شده است",
        "blank": "نام کاربری نمی تواند خالی باشد",
        "null": "نام کاربری نمی تواند خالی باشد",
    })
    email = models.EmailField(unique=True, max_length=200, blank=False, null=False, validators=[validate_email, ],
                              error_messages={
                                  "unique": "این ایمیل قبلا استفاده شده است",
                                  "blank": "ایمیل نمیتواند خالی باشد",
                                  "null": "نام کاربری نمی تواند خالی باشد",
                              })
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    phone = models.CharField(max_length=11, blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]

    def __str__(self):
        return self.email

