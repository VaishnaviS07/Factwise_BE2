# app/models.py
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=64, unique=True)
    display_name = models.CharField(max_length=64)
    creation_time = models.DateTimeField(auto_now_add=True)

class Team(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.CharField(max_length=128)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    creation_time = models.DateTimeField(auto_now_add=True)

class ProjectBoard(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=128)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    creation_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default="OPEN")

class Task(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=128)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    board = models.ForeignKey(ProjectBoard, on_delete=models.CASCADE)
    creation_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default="OPEN")
