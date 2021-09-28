from rest_framework import serializers
from .models import Cozinheiro

class CozinheiroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cozinheiro
        fields = ['username', 'email', 'experiencia', 'password']
        read_only_fields = ['experiencia']

class ResgisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cozinheiro
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        user = Cozinheiro.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user
