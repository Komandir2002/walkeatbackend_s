from walkeat import settings
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
import jwt
from phonenumber_field.modelfields import PhoneNumberField
from datetime import datetime, timedelta



class MyUserManager(BaseUserManager):


    def _create_user(self, email, phone, username, password, **extra_fields):

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
        if user.is_superuser:
            self.model(
                email=self.normalize_email(email),
                username=username,
                phone=phone,
                **extra_fields,
            )

            user.set_password(password)
            user.save(using=self._db)
            return user
        user.set_password(password)
        user.save(using=self._db)

        return user


    def create_user(self, email, phone, username, password):
        return self._create_user(email, phone, username, password)

    def create_superuser(self, email, username, password, phone = None):
            return self._create_user(email, phone, username, password,is_staff=True, is_superuser=True)



class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True, unique=True)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    phone = PhoneNumberField(unique=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = ["email", "username"]
    if is_staff:
        USERNAME_FIELD = "username"
        REQUIRED_FIELDS = ["email", "phone"]


    objects = MyUserManager()

    def __str__(self):
        return self.email

    @property
    def token(self):
        return self._generate_jwt_token()

    def _generate_jwt_token(self):
        dt = datetime.now() + timedelta(days=1)

        token = jwt.encode(
            {"id": self.pk, "exp": int(dt.strftime("%s"))},
            settings.SECRET_KEY,
            algorithm="HS256",
        )

        return token
