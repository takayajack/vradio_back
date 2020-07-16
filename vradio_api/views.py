from django.shortcuts import render
from rest_framework import viewsets
from .models import Vtuber
from .serializers import VtuberSerializer

# Create your views here.
class VtuberViewSet(viewsets.ModelViewSet):
  queryset = Vtuber.objects.all()
  serializer_class = VtuberSerializer
