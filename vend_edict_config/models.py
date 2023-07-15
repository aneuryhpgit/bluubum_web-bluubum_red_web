from django.db import models

from django.contrib.auth.models import User

class Email_temporal(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_temp = models.EmailField(blank=True, null=True)

# Create your models here.
