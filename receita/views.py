from django.db import models
from django.shortcuts import render
from rest_framework import viewsets, permissions, generics
from .serializers import ReceitaSerializer, CategoriaSerializer
from receita import models
from rest_framework.filters import SearchFilter, OrderingFilter


class ReceitaViewSet(viewsets.ModelViewSet):
    serializer_class = ReceitaSerializer
    queryset = models.Receita.objects.all()
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('nome_receita', 'categoria_receita__nome_categoria')


class CategoriaViewSet(viewsets.ModelViewSet):
    serializer_class = CategoriaSerializer
    queryset = models.Categoria.objects.all()
