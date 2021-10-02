
from rest_framework import routers
from dica import views as dicasviewsets
from django.urls import path
from django.urls.conf import include

app_name = "dica"
route = routers.DefaultRouter()

route.register(r'', dicasviewsets.DicaViewSet, basename='dicas')


urlpatterns = [
    path('', include(route.urls)),
]
