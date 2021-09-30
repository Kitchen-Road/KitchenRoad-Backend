from django.db import models
from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import DicaSerializer
from dica import models


class DicaViewSet(viewsets.ModelViewSet):
    serializer_class = DicaSerializer
    queryset = models.Dica.objects.all()
