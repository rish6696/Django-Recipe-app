from lib2to3.pytree import Base
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                                               PermissionsMixin


class UserManager(BaseUserManager):

    def create_user(self,email,password = None, **extra_fields):
        """Create and save the new user"""

        if not email:
            raise ValueError("Email should be passed")

        user = self.model(email= self.normalize_email(email), **extra_fields)
        user.set_password(password)

        user.save(using= self._db)
        return user;

class User (AbstractBaseUser,PermissionsMixin):
    """custom user model that supports """
    email = models.EmailField(max_length=255,unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD ='email'


