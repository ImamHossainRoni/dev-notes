from typing import List
from user_model import User
from user_repository_interface import UserRepositoryInterface


class UserRepository(UserRepositoryInterface):
    def __init__(self, users: List[User]):
        self.users = users

    def get_all_users(self) -> List[User]:
        return self.users

    def get_user_by_id(self, user_id: int) -> User:
        return next((user for user in self.users if user.id == user_id))

    def create_user(self, user: User) -> User:
        user.id = len(self.users) + 1
        user.name = "Imam Hossain Roni"
        self.users.append(user)
