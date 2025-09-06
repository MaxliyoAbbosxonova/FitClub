from django.contrib import admin

from apps.accounts.models import Profile, User, EmailVerification

# Register your models here.
admin.site.register([Profile,User,EmailVerification])