from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics
from accounts.serializers import UserProfileSerializer


# Create your views here.


class GetUserView(generics.ListCreateAPIView):
    queryset = User.objects.select_related('profile').all()
    serializer_class = UserProfileSerializer

class DetailUserView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.select_related('profile').all()
    serializer_class = UserProfileSerializer

