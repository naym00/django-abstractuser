from django.db import models
from django.contrib.auth.models import AbstractUser

class Nuser(AbstractUser):
    phone = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=10, choices=(('Male', 'Male'), ('Female', 'Female')))
    def __str__(self):
        return f'{self.username} - {self.is_superuser}'