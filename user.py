# app/concrete_classes/user.py
from app.base_classes.user_base import UserBase
from app.models import User
from django.core.exceptions import ValidationError
import json

class UserConcrete(UserBase):

    def create_user(self, request: str) -> str:
        data = json.loads(request)
        try:
            user = User.objects.create(
                name=data['name'],
                display_name=data['display_name']
            )
            return json.dumps({"id": user.id})
        except ValidationError as e:
            raise Exception(f"Invalid input: {e}")

    def list_users(self) -> str:
        users = User.objects.all().values('name', 'display_name', 'creation_time')
        return json.dumps(list(users))

    def describe_user(self, request: str) -> str:
        data = json.loads(request)
        user = User.objects.get(id=data['id'])
        response = {
            "name": user.name,
            "display_name": user.display_name,
            "creation_time": user.creation_time
        }
        return json.dumps(response)

    def update_user(self, request: str) -> str:
        data = json.loads(request)
        user = User.objects.get(id=data['id'])
        user.display_name = data['user']['display_name']
        user.save()
        return json.dumps({"status": "updated"})

    def get_user_teams(self, request: str) -> str:
        data = json.loads(request)
        user = User.objects.get(id=data['id'])
        teams = user.team_set.all().values('name', 'description', 'creation_time')
        return json.dumps(list(teams))
