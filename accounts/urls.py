from django.urls import path
from .views import CreateAccountView


urlpatterns = [path("accounts/", CreateAccountView.as_view())]
