# app/views.py
from rest_framework import viewsets
from app.models import User, Team, ProjectBoard, Task
from app.serializers import UserSerializer, TeamSerializer, ProjectBoardSerializer, TaskSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class ProjectBoardViewSet(viewsets.ModelViewSet):
    queryset = ProjectBoard.objects.all()
    serializer_class = ProjectBoardSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
