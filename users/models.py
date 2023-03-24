from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    birthdate = models.DateField()
    date_updated = models.DateTimeField(auto_now=True)
    email = models.EmailField()

    REQUIRED_FIELDS = ['birthdate', ]
