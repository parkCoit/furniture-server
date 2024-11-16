from datetime import datetime

from sqlalchemy import Column, String, DateTime, ForeignKey
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

    def __str__(self):
        return f'index: {self.kakao_id}, \n '


class UserToken(Base):
    __tablename__ = "user_token"
    kakao_id = Column(String(50), ForeignKey('users.kakao_id'), primary_key=True)  # 카카오 ID
    access_token = Column(String(100), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)  # 생성 시각
    # refresh_token = Column(String(100), nullable=False)  # refresh_token
    # access_token_expiry = Column(DateTime, nullable=False)  # access_token 만료 시간
    # refresh_token_expiry = Column(DateTime, nullable=False)  # refresh_token 만료 시간

    user = relationship("User", back_populates="tokens")

    class Config:
        arbitrary_types_allowed = True

    def __str__(self):
        return f'index: {self.userid}, \n '