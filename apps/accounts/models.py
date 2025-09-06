from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models



class User(AbstractUser):
    email = models.EmailField(unique=True,null=False,blank=False)

    phone_regex = RegexValidator(
            regex=r'^\+998\d{9}$',
            message="Telefon raqam '+998901234567' formatida kiritilishi kerak."
        )
    phone = models.CharField(max_length=15, unique=True,validators=[phone_regex])

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username',"phone"]

    def __str__(self):
        return self.phone

class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    birth=models.CharField(null=True,blank=True)
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}: {self.birth}"


class EmailVerification(models.Model):
    user=models.OneToOneField(User, related_name='email_verification', on_delete=models.CASCADE)
    code=models.CharField(max_length=50)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.email

