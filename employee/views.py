from django.shortcuts import render
from rest_framework import viewsets
from .models import EmployeeData
from .serializer import EmployeeSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = EmployeeData.objects.all()
    serializer_class = EmployeeSerializer


# Create your views here.
