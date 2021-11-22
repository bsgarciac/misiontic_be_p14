from rest_framework import serializers
from .models import Soporte, PQR, Bank
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class SoporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Soporte
        fields = '__all__'


class PQRSerializer(serializers.ModelSerializer):
    soporte = SoporteSerializer(read_only=True)

    class Meta:
        model = PQR
        fields = ['id', 'soporte', 'tipo', 'info']


class BankSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True)

    class Meta:
        model = Bank
        fields = ['id', 'name', 'users']
