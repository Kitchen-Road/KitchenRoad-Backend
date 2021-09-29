from django.db import models
from django.shortcuts import render
from rest_framework import viewsets, permissions, generics
from rest_framework.filters import SearchFilter, OrderingFilter
from .serializers import ReceitaSerializer, CategoriaSerializer
from receita import models


class ReceitaViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ReceitaSerializer
    queryset = models.Receita.objects.all()
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = (
        'nome_receita', 'categoria_receita__nome_categoria', 'dificuldade')


class CategoriaViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = CategoriaSerializer
    queryset = models.Categoria.objects.all()
