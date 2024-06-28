from typing import Optional

from pydantic import BaseModel


class FurnitureVo(BaseModel):
    class Config:
        arbitrary_types_allowed = True


class FurnitureDTO(FurnitureVo):
    id: Optional[int]  # 제거해야함 auto로 사용 시
    name: Optional[str]
    color: Optional[str]
    material: Optional[str]
    size: Optional[str]
    style: Optional[str]

    def __str__(self):
        return f'id: {self.name},' \

