# app/urls.py
from django.urls import path
from app.views import TeamView, UserView, ProjectBoardView

urlpatterns = [
    path('api/teams/', TeamView.as_view(), name='teams'),
    path('api/users/', UserView.as_view(), name='users'),
    path('api/project-boards/', ProjectBoardView.as_view(), name='project_boards'),
]

