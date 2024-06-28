
from abc import abstractmethod, ABCMeta
from typing import List

from app.schemas.furniture import FurnitureVo


class FurnitureBase(metaclass=ABCMeta):
    @abstractmethod
    def create_furniture(self, request: FurnitureVo): pass

    def read_furniture(self, furniture_id: int): pass

    def update_furniture(self, furniture_id: int, request: FurnitureVo): pass

    def delete_furniture(self, furniture_id: int): pass
