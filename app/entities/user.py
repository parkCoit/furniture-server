from sqlalchemy import Column, String

from app.database import Base


class User(Base):
    __tablename__ = "users"
    userid = Column(String(50), nullable=False, primary_key=True)
    password = Column(String(100), nullable=False)
    token = Column(String(256))

    class Config:
        arbitrary_types_allowed = True

    def __str__(self):
        return f'index: {self.userid}, \n '


