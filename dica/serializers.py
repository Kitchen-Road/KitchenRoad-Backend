from django.db.models import fields
from .models import Dica
from rest_framework import serializers


class DicaSerializer(serializers.ModelSerializer):
    class Meta():
        model = Dica
        fields = '__all__'

