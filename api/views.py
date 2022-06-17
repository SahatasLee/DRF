from django.shortcuts import render
from .serializers import TaskSerializer
from .models import Task
from rest_framework import generics


class TaskList(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskDetails(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer