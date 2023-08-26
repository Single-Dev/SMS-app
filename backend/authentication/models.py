from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(
        verbose_name='email address',
        max_length=250,
        unique=True,
    )
    username = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=200, blank=True)
    last_name = models.CharField(max_length=200, blank=True)
    is_admin = models.BooleanField(default=False)
    
    def __str__(self):
        return self.username

    class Meta:
        ordering = ['-id']
        # (-) yoki (+) modellar ro'yahti qanday tuzish keark ekanligiga ta'sir qiladi
