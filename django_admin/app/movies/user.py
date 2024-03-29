import uuid

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from movies import models


class Roles:
    ADMIN = "admin"
    SUPER_ADMIN = "super_admin"
    USER = "user"


class CustomUserManager(BaseUserManager):
    def create_user(self, login, password=None):
        if not login:
            raise ValueError("User")

        user = self.model(login=login)
        user.set_password(password)
        user.email = self.normalize_email(user.email)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(email, password)
        user.is_admin = True
        user.save(using=self._db)
        return user
