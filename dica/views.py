from django.db import models
from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import DicaSerializer
from dica import models
import random


def pick_random_object():
    return random.randrange(1, models.Dica.objects.all().count() + 1)


class DicaViewSet(viewsets.ModelViewSet):
    serializer_class = DicaSerializer

    def get_queryset(self):
        return models.Dica.objects.all().filter(id=pick_random_object())
