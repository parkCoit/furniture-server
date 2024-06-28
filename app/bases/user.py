
from abc import abstractmethod, ABCMeta
from typing import List

from app.schemas.user import UserDTO


class UserBase(metaclass=ABCMeta):
    @abstractmethod
    def add_user(self, request_user: UserDTO): pass

    def get_user(self): pass
