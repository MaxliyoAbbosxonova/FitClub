from django.urls import path
import apps.accounts.views as views

urlpatterns=[
    path('users/', views.GetUserView.as_view()),
    path('detail_u/<int:pk>', views.DetailUserView.as_view()),
    path('test-email/', views.test_email),
    path('confirm-email', views.VerifyEmailView.as_view()),
]



