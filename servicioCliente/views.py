from django.shortcuts import render
from rest_framework import generics
from .models import PQR, Soporte
from .serializer import SoporteSerializer, PQRSerializer
# Create your views here.


class SoporteListCreate(generics.ListCreateAPIView):
    queryset = Soporte.objects.all()
    serializer_class = SoporteSerializer

class SoporteUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Soporte.objects.all()
    serializer_class = SoporteSerializer

class PQRListCreate(generics.ListCreateAPIView):
    queryset = PQR.objects.all()
    serializer_class = PQRSerializer

class PQRUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = PQR.objects.all()
    serializer_class = PQRSerializer
