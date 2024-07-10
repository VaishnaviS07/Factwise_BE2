# app/urls.py
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from app.views import UserViewSet, TeamViewSet, ProjectBoardViewSet, TaskViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'boards', ProjectBoardViewSet)
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
