from django.db import models
from django.contrib.auth.models import (
  BaseUserManager,
  AbstractUser,
)


class UserManager(BaseUserManager):
  def create_user(self, email, password, **extra_fields):
    if not email:
      raise ValueError('The email field is required')
    email = self.normalize_email(email)
    user = self.model(email=email, **extra_fields)
    user.set_password(password)
    user.save()
    return user

  def create_superuser(self, email, password, **extra_fields):
    extra_fields.setdefault('is_staff', True)
    extra_fields.setdefault('is_superuser', True)
    extra_fields.setdefault('is_active', True)

    if not extra_fields.get('is_superuser'):
      raise ValueError('Superuser must have is_staff=True.')
    if not extra_fields.get('is_staff'):
      raise ValueError('Is staff must have is_staff=True.')
    return self.create_user(email, password, **extra_fields)
  

class User(AbstractUser):
  username = None
  email = models.EmailField(unique=True)

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = []

  objects = UserManager()

  def __str__(self) -> str:
    return self.email
