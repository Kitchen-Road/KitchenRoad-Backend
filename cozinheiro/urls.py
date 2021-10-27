from django.urls import path
from django.urls.conf import include
from rest_framework import routers
from .views import ReceitaListViewSet, RegisterCozinheiroView, LoginCozinheiroView, ReceitaCompletadaView

app_name = "cozinheiro"

urlpatterns = [
    path('signup/', RegisterCozinheiroView.as_view(), name="signup"),
    path('login/', LoginCozinheiroView.as_view(), name="login"),
    path('concluir-receita/', ReceitaCompletadaView.as_view(),
         name="concluir_receita"),
    path('listar-concluidas/', ReceitaListViewSet.as_view(),
         name="listar-concluidas"),
]
