from django.db.models import fields
from .models import Conquista
from rest_framework import serializers


class ConquistaSerializer(serializers.ModelSerializer):
    class Meta():
        model = Conquista
        fields = '__all__'
