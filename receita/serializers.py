from django.db.models import fields
from .models import Epoca, Receita, Categoria
from rest_framework import serializers


class ReceitaSerializer(serializers.ModelSerializer):
    class Meta():
        model = Receita
        fields = '__all__'


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta():
        model = Categoria
        fields = '__all__'


class EpocaSerializer(serializers.ModelSerializer):
    class Meta():
        model = Epoca
        fields = '__all__'
