from datetime import datetime
from zoneinfo import ZoneInfo

from sqlalchemy import Column, String, DateTime, ForeignKey, Integer
from sqlalchemy.orm import relationship

from app.database import Base


class User(Base):
    __tablename__ = "users"

    kakao_id = Column(String(50), primary_key=True, nullable=False, unique=True)
    email = Column(String(50), unique=True, nullable=True)
    nickname = Column(String(50))

    tokens = relationship("UserToken", back_populates="user")

    class Config:
        arbitrary_types_allowed = True
        from_attributes = True
        orm_mode = True

    def __str__(self):
        return f'index: {self.kakao_id}, \n '


class UserToken(Base):
    __tablename__ = "user_token"
    id = Column(Integer, primary_key=True, autoincrement=True)
    access_token = Column(String(255), nullable=False, unique=True)
    kakao_id = Column(String(50), ForeignKey('users.kakao_id'))
    created_at = Column(DateTime, default=datetime.now(ZoneInfo("Asia/Seoul")))

    user = relationship("User", back_populates="tokens")

    class Config:
        arbitrary_types_allowed = True
        from_attributes = True
        orm_mode = True

    def __str__(self):
        return f'index: {self.userid}, \n '