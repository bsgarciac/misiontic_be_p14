from django.shortcuts import render
from rest_framework import views, generics, authentication, permissions, status
from .models import PQR, Soporte, Bank
from rest_framework.response import Response
from .serializer import SoporteSerializer, PQRSerializer, BankSerializer
from django.contrib.auth.models import User

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


class CountUser(views.APIView):
    def get(self, request):
        print("Para acceder al body de la peticion es con request.data")
        queryset = User.objects.all()
        for user in queryset:
            print(user.username)
        con_users = len(queryset)
        data={"Number of users": con_users}
        return Response(data=data, status=status.HTTP_200_OK)
