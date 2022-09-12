from django.db import models
from django.contrib.auth.models import (
    AbstractUser,
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
)

from phonenumber_field.modelfields import PhoneNumberField
# from creditcards.models import CardNumberField, CardExpiryField, SecurityCodeField
from walkeat import settings


# class Card(models.Model):
#     user = models.OneToOneField(
#         settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_card"
#     )
#     cc_number = CardNumberField("card number")
#     cc_expiry = CardExpiryField("expiration date")
#     cc_code = SecurityCodeField("security code")
#
#     def __str__(self):
#         return f"{self.cc_number} {self.user} card"
#

class MyUserManager(BaseUserManager):
    def _create_user(self, email, username, password, phone, **extra_fields):
        if not email:
            raise ValueError("Вы не ввели Email")
        if not username:
            raise ValueError("Вы не ввели Логин")
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            phone=phone,
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, username, password, phone):
        return self._create_user(email, username, password, phone)

    def create_superuser(self, email, username, password, phone):
        return self._create_user(
            email, username, password, phone, is_staff=True, is_superuser=True
        )


class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True, unique=True)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    photo = models.ImageField(
        default="media/avatar.jpeg", upload_to="uploaded_media", blank=True
    )
    birthday = models.DateField(blank=True, null=True)
    phone = PhoneNumberField(unique=True)
    # card = models.ForeignKey(
    # Card, on_delete=models.CASCADE, null=True, related_name="user_card"
    # )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = ["email", "username"]
    objects = MyUserManager()

    def __str__(self):
        return self.email