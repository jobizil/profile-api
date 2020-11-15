from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin,  BaseUserManager



class UserProfileManager(BaseUserManager):
    """  Manager for user profiles """
    def create_user(self, email, name, password=None):
        """ Creates a new user Profile """
        if not email:
            raise ValueError('Email address is required')

        # Normalize the email Address
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """ Create and save a new superuser with given details """
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """[DB Model for Users] AbstractBaseUser & PermissionsMixin: Are used for overwriting the default Django user model """
    name = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserProfileManager()

    # Allows user to provide emails as signin option instead of username
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Gets full name of user  """
        return self.name

    def get_short_name(self):
        return self.name

    def __str__(self):
        return self.email
