from sqlalchemy import Column, String, Integer

from app.database import Base


class Furniture(Base):
    __tablename__ = "furnitures"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(50), index=True)
    color = Column(String(50))
    material = Column(String(50))
    size = Column(String(50))
    style = Column(String(50))

    class Config:
        arbitrary_types_allowed = True

    def __str__(self):
        return f'index: {self.id}, \n '


