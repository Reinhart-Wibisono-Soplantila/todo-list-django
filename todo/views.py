from django.shortcuts import render
from rest_framework import viewsets
from .models import ToDo
from .serializers import ToDoSerializers

# Create your views here.
class ToDoViewSet(viewsets.ModelViewSet):
    queryset=ToDo.objects.all()
    serializer_class=ToDoSerializers