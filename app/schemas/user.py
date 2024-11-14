from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class UserVo(BaseModel):
    class Config:
        arbitrary_types_allowed = True
        orm_mode = True


class UserDTO(UserVo):
    kakaoid: Optional[str]
    email: Optional[str]
    nickname: Optional[str]

    def __str__(self):
        return f'userid: {self.kakaoid},' \
               f'email: {self.email}' \
               f'nickname: {self.nickname}' \



class UserTokenVo(BaseModel):
    class Config:
        arbitrary_types_allowed = True
        orm_mode = True


class UserTokenDTO(UserVo):
    kakaoid: str
    access_token: str
    refresh_token: str
    access_token_expiry: datetime
    refresh_token_expiry: datetime
    created_at: datetime

    def __str__(self):
        return f'kakaoid: {self.kakaoid}, access_token: {self.access_token}, ' \
               f'refresh_token: {self.refresh_token}, ' \
               f'access_token_expiry: {self.access_token_expiry}, ' \
               f'refresh_token_expiry: {self.refresh_token_expiry}'

