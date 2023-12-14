from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer
from django.contrib.auth.mixins import LoginRequiredMixin

class TaskViewSet(LoginRequiredMixin, viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer