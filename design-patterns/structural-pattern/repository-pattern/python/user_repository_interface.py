from abc import ABC, abstractmethod
from typing import List

from user_model import User


class UserRepositoryInterface(ABC):
    @abstractmethod
    def get_all_users(self) ->List[User]:
        pass

    @abstractmethod
    def get_user_by_id(self, user_id: int) -> User:
        pass

    @abstractmethod
    def create_user(self, user:User) -> User:
        pass