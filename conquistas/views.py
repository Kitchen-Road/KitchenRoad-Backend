from django.db import models
from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import ConquistaSerializer
from conquistas import models


class ConquistaViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ConquistaSerializer
    queryset = models.Conquista.objects.all()
