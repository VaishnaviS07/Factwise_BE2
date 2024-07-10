# app/concrete_classes/team.py
from app.base_classes.team_base import TeamBase
from app.models import Team, User
from django.core.exceptions import ValidationError
import json

class TeamConcrete(TeamBase):

    def create_team(self, request: str) -> str:
        data = json.loads(request)
        try:
            team = Team.objects.create(
                name=data['name'],
                description=data['description'],
                admin=User.objects.get(id=data['admin'])
            )
            return json.dumps({"id": team.id})
        except ValidationError as e:
            raise Exception(f"Invalid input: {e}")

    def list_teams(self) -> str:
        teams = Team.objects.all().values('name', 'description', 'creation_time', 'admin')
        return json.dumps(list(teams))

    def describe_team(self, request: str) -> str:
        data = json.loads(request)
        team = Team.objects.get(id=data['id'])
        response = {
            "name": team.name,
            "description": team.description,
            "creation_time": team.creation_time,
            "admin": team.admin.id
        }
        return json.dumps(response)

    def update_team(self, request: str) -> str:
        data = json.loads(request)
        team = Team.objects.get(id=data['id'])
        team.name = data['team']['name']
        team.description = data['team']['description']
        team.admin = User.objects.get(id=data['team']['admin'])
        team.save()
        return json.dumps({"status": "updated"})

    def add_users_to_team(self, request: str):
        data = json.loads(request)
        team = Team.objects.get(id=data['id'])
        users = User.objects.filter(id__in=data['users'])
        if users.count() + team.users.count() > 50:
            raise Exception("Exceeds maximum users limit")
        team.users.add(*users)
        return json.dumps({"status": "users added"})

    def remove_users_from_team(self, request: str):
        data = json.loads(request)
        team = Team.objects.get(id=data['id'])
        users = User.objects.filter(id__in=data['users'])
        team.users.remove(*users)
        return json.dumps({"status": "users removed"})

    def list_team_users(self, request: str):
        data = json.loads(request)
        team = Team.objects.get(id=data['id'])
        users = team.users.all().values('id', 'name', 'display_name')
        return json.dumps(list(users))
