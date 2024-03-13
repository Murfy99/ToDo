from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, generics
from .models import TODO
from .serializers import TODOSerializer
from rest_framework.generics import get_object_or_404

# Create your views here.
class ListTODOView(generics.CreateAPIView):
    queryset = TODO.objects.all()
    serializer_class = TODOSerializer

class AddTODOView(generics.CreateAPIView):
    queryset = TODO.objects.all()
    serializer_class = TODOSerializer

class UpdateTODOView(generics.UpdateAPIView):
    queryset = TODO.objects.all()
    serializer_class = TODOSerializer
    lookup_field = 'id'

class DeleteTODOView(generics.DestroyAPIView):
    queryset = TODO.objects.all()
    serializer_class = TODOSerializer
    lookup_field = 'id'