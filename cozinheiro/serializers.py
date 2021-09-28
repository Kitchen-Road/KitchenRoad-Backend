from rest_framework import serializers
from .models import Cozinheiro

class CozinheiroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cozinheiro
        fields = ['username', 'email', 'password', 'experiencia']
        extra_kwargs = {'password': {'write_only': True}}
        read_only_fields = ['experiencia']