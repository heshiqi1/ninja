from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
class UserModel(models.Model):
    username = models.CharField(unique=True, max_length=100, blank=False)
    email = models.EmailField(max_length=100, blank=True)
    password = models.CharField(max_length=100, blank=False)


class UserToken(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.UUIDField(default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return str(self.token)