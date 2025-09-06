from django.core.mail import send_mail
from django.http import HttpResponse
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.accounts.models import User, EmailVerification
from apps.accounts.serializers import UserProfileSerializer, VerifyEmailSerializer


# Create your views here.


class GetUserView(generics.ListCreateAPIView):
    queryset = User.objects.select_related('profile').all()
    serializer_class = UserProfileSerializer

class DetailUserView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.select_related('profile').all()
    serializer_class = UserProfileSerializer



def test_email(request):
       send_mail(
        'Test',
           'Message test',
           'makhliyoabboskhonova@gmail.com',
           [request.user.get_email_field_name()],
            fail_silently=False,

       )
       return HttpResponse('Test email yuborildi')

class VerifyEmailView(APIView):
    serializer_class = VerifyEmailSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data["email"]
        code = serializer.validated_data["code"]

        try:
            verification = EmailVerification.objects.get(user__email=email, code=code)
            user = verification.user
            user.is_active = True
            user.save()
            verification.delete()
            return Response({"message": "Email tasdiqlandi ✅"}, status=status.HTTP_200_OK)
        except EmailVerification.DoesNotExist:
            return Response({"error": "Kod noto‘g‘ri ❌"}, status=status.HTTP_400_BAD_REQUEST)