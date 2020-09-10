from django.shortcuts import render
from rest_framework import viewsets
from .models import Vtuber,Type
from .serializers import VtuberSerializer,TypeSerializer

# Create your views here.
class VtuberViewSet(viewsets.ModelViewSet):
  queryset = Vtuber.objects.all()
  serializer_class = VtuberSerializer

class TypeViewSet(viewsets.ModelViewSet):
  queryset = Type.objects.all()
  serializer_class = TypeSerializer