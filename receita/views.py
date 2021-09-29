from django.db import models
from django.shortcuts import render
from rest_framework import viewsets, permissions, generics
from .serializers import ReceitaSerializer, CategoriaSerializer
from receita import models
from .models import Receita


class ReceitaViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ReceitaSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_staff or user.experiencia == 'A':
            return Receita.objects.all()
        else:
            if user.experiencia == 'I':
                return Receita.objects.filter(dificuldade=user.experiencia)
            else:
                return Receita.objects.exclude(dificuldade='A')


class CategoriaViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = CategoriaSerializer
    queryset = models.Categoria.objects.all()
