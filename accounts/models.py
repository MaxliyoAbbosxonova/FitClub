from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
    phone = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True, null=True, blank=True)

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = ['username',"email"]

    def __str__(self):
        return self.phone

class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    birth=models.CharField(null=True,blank=True)
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}: {self.birth}"