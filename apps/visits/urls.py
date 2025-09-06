from django.urls import path

from apps.accounts import views

urlpatterns = [
path('accounts/users/', views.GetUserView.as_view()),
path('accounts/U_detail/', views.DetailUserView.as_view()),

]