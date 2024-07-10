# app/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json
from app.concrete_classes.team import TeamConcrete
from app.concrete_classes.user import UserConcrete
from app.concrete_classes.project_board import ProjectBoardConcrete

class TeamView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            team = TeamConcrete()
            result = team.create_team(request.body.decode('utf-8'))
            return Response(json.loads(result), status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        team = TeamConcrete()
        result = team.list_teams()
        return Response(json.loads(result), status=status.HTTP_200_OK)


class UserView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            user = UserConcrete()
            result = user.create_user(request.body.decode('utf-8'))
            return Response(json.loads(result), status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        user = UserConcrete()
        result = user.list_users()
        return Response(json.loads(result), status=status.HTTP_200_OK)


class ProjectBoardView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            board = ProjectBoardConcrete()
            result = board.create_board(request.body.decode('utf-8'))
            return Response(json.loads(result), status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        board = ProjectBoardConcrete()
        result = board.list_boards(request.body.decode('utf-8'))
        return Response(json.loads(result), status=status.HTTP_200_OK)
