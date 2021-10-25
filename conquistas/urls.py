
from rest_framework import routers
from conquistas import views as conquistasviewsets
from django.urls import path
from django.urls.conf import include

app_name = "conquistas"
route = routers.DefaultRouter()

route.register(r'', conquistasviewsets.ConquistaViewSet, basename='conquistas')


urlpatterns = [
    path('', include(route.urls)),
]
