# app/serializers.py
from rest_framework import serializers
from app.models import User, Team, ProjectBoard, Task

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'display_name', 'creation_time']

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'name', 'description', 'creation_time', 'admin']

class ProjectBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectBoard
        fields = ['id', 'name', 'description', 'team', 'creation_time', 'status']

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'user', 'board', 'creation_time', 'status']
