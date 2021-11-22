from django.shortcuts import render
from rest_framework import views, generics, authentication, permissions, status
from .models import PQR, Soporte, Bank
from rest_framework.response import Response
from .serializer import SoporteSerializer, PQRSerializer, BankSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework import views, authentication, permissions, status

# Create your views here.


class SoporteListCreate(generics.ListCreateAPIView):
    queryset = Soporte.objects.all()
    serializer_class = SoporteSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class SoporteUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Soporte.objects.all()
    serializer_class = SoporteSerializer

class PQRListCreate(generics.ListCreateAPIView):
    queryset = PQR.objects.all()
    serializer_class = PQRSerializer

class PQRUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = PQR.objects.all()
    serializer_class = PQRSerializer

class BankListCreate(generics.ListCreateAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer


class UserRetrieve(views.APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
