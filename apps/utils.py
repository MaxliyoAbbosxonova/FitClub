import uuid

from django.core.mail import send_mail

from root import settings


def generate_verification_code():
    return str(uuid.uuid4())[:6]

def send_verification_email(user,code):
    subject = "Emailingizni tasdiqlang"
    message = f"Sizning tasdiqlash kodingiz: {code}"
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email])
    # if  views.VerifyEmailView.post.correct==True:
    #     message="Email tasdiqlandi"
    #     send_mail(subject, settings.DEFAULT_FROM_EMAIL, [user.email])
    #
