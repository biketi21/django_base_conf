from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)

# Create your models here.


class AccountManager(BaseUserManager):
    def create_user(self, firstname, email, password=None):
        if not email:
            raise ValueError("User must register with an email address")
        if not firstname:
            raise ValueError("User should provide Username.")

        user = self.model(email=self.normalize_email(email), firstname=firstname)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, firstname, password):
        user = self.model(email=self.normalize_email(email), firstname=firstname)
        user.set_password(password)

        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)

        return user


class Account(AbstractBaseUser, PermissionsMixin):
    firstname = models.CharField(max_length=30)
    email = models.EmailField(max_length=30, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = AccountManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["firstname"]

    def __str__(self):
        return str(self.email)
