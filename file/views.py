from django.shortcuts import render
from rest_framework import generics
from .serializers import FileSerializer
from .models import File


class FileView(generics.CreateAPIView):
    serializer_class = FileSerializer
    queryset = File.objects.all()
