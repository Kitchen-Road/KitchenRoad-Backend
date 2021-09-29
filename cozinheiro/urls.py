from django.urls import path
from django.urls.conf import include
from rest_framework import routers
from .views import RegisterCozinheiroView, LoginCozinheiroView

app_name = "cozinheiro"

urlpatterns = [
    path('signup/', RegisterCozinheiroView.as_view(), name="signup"),
    path('login/', LoginCozinheiroView.as_view(), name="login"),
]
