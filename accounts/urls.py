from django.urls import path
import accounts.views

urlpatterns=[
    path('users/',accounts.views.GetUserView.as_view()),
    path('detail_u/<int:pk>',accounts.views.DetailUserView.as_view()),
]



