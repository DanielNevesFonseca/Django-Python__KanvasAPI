from django.urls import path
from .views import CreateAccountView, LoginJWTView

urlpatterns = [
    path("accounts/", CreateAccountView.as_view()),
    path("login/", LoginJWTView.as_view()),
]
