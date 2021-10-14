from django.db import models
from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.filters import SearchFilter, OrderingFilter
from .serializers import EpocaSerializer, ReceitaSerializer, CategoriaSerializer
from receita import models


class ReceitaViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ReceitaSerializer

    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = (
        'nome_receita', 'categoria_receita__nome_categoria', 'epoca__nome_epoca')

    def get_queryset(self):
        queryset = models.Receita.objects.all()
        query = self.request.GET.get("dificuldade")
        if query:
            queryset = queryset.filter(dificuldade=query).distinct()
        return queryset


class CategoriaViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = CategoriaSerializer
    queryset = models.Categoria.objects.all()


class EpocaViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = EpocaSerializer
    queryset = models.Epoca.objects.all()
