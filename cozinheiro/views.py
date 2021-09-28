from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CozinheiroSerializer
from .models import Cozinheiro

class CozinheiroViewSet(viewsets.ModelViewSet):
    serializer_class = CozinheiroSerializer
    queryset = Cozinheiro.objects.all()