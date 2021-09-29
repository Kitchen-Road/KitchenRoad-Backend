
from rest_framework import routers
from receita import views as receitasviewsets
from django.urls import path
from django.urls.conf import include

app_name = "receita"
route = routers.DefaultRouter()

route.register(r'', receitasviewsets.ReceitaViewSet, basename='listReceita')


urlpatterns = [
    path('', include(route.urls)),
]
