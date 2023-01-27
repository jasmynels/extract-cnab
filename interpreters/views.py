from django.shortcuts import render
from rest_framework import generics
from .serializers import InterpreterSerializer
from .models import Interpreter
from django_filters import rest_framework as filters
from .pagination import CustomPagination


class InterpreterFilter(filters.FilterSet):
    store_name = filters.CharFilter(
        field_name="store_name", lookup_expr="icontains"
    )

    class Meta:
        model = Interpreter
        fields = ["store_name"]


class InterpreterView(generics.ListCreateAPIView):
    serializer_class = InterpreterSerializer
    queryset = Interpreter.objects.all()
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = InterpreterFilter
