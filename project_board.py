# app/concrete_classes/project_board.py
from app.base_classes.project_board_base import ProjectBoardBase
from app.models import ProjectBoard, Task, Team, User
from django.core.exceptions import ValidationError
import json
import datetime

class ProjectBoardConcrete(ProjectBoardBase):

    def create_board(self, request: str):
        data = json.loads(request)
        try:
            team = Team.objects.get(id=data['team_id'])
            board = ProjectBoard.objects.create(
                name=data['name'],
                description=data['description'],
                team=team,
                creation_time=datetime.datetime.strptime(data['creation_time'], "%Y-%m-%d %H:%M:%S")
            )
            return json.dumps({"id": board.id})
        except ValidationError as e:
            raise Exception(f"Invalid input: {e}")

    def close_board(self, request: str) -> str:
        data = json.loads(request)
        board = ProjectBoard.objects.get(id=data['id'])
        if not Task.objects.filter(board=board, status__in=["OPEN", "IN_PROGRESS"]).exists():
            board.status = "CLOSED"
            board.save()
            return json.dumps({"status": "closed"})
        else:
            raise Exception("Cannot close board with incomplete tasks")

    def add_task(self, request: str) -> str:
        data = json.loads(request)
        try:
            board = ProjectBoard.objects.get(id=data['board_id'], status="OPEN")
            user = User.objects.get(id=data['user_id'])
            task = Task.objects.create(
                title=data['title'],
                description=data['description'],
                user=user,
                board=board,
                creation_time=datetime.datetime.strptime(data['creation_time'], "%Y-%m-%d %H:%M:%S")
            )
            return json.dumps({"id": task.id})
        except ValidationError as e:
            raise Exception(f"Invalid input: {e}")

    def update_task_status(self, request: str):
        data = json.loads(request)
        task = Task.objects.get(id=data['id'])
        task.status = data['status']
        task.save()
        return json.dumps({"status": "updated"})

    def list_boards(self, request: str) -> str:
        data = json.loads(request)
        boards = ProjectBoard.objects.filter(team_id=data['id'], status="OPEN").values('id', 'name')
        return json.dumps(list(boards))

    def export_board(self, request: str) -> str:
        data = json.loads(request)
       
