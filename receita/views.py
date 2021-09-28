from django.db import models
from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import ReceitaSerializer, CategoriaSerializer
from receita import models

class ReceitaViewSet(viewsets.ModelViewSet):
    serializer_class = ReceitaSerializer
    queryset =  models.Receita.objects.all()

class CategoriaViewSet(viewsets.ModelViewSet):
    serializer_class = CategoriaSerializer
    queryset =  models.Categoria.objects.all()