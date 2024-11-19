from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class UserVo(BaseModel):
    class Config:
        arbitrary_types_allowed = True
        from_attributes = True
        orm_mode = True


class UserDTO(UserVo):
    code: Optional[object]

    def __str__(self):
        return f'code : {self.code}'

class UserTokenVo(BaseModel):
    class Config:
        arbitrary_types_allowed = True
        from_attributes = True
        orm_mode = True


class UserTokenDTO(UserVo):
    kakao_id: str
    access_token: str
    created_at: datetime
    # refresh_token: str
    # access_token_expiry: datetime
    # refresh_token_expiry: datetime

    def __str__(self):
        return f'kakaoid: {self.kakaoid}, access_token: {self.access_token}, ' \
               f'access_token_expiry: {self.access_token_expiry}, ' \
               # f'refresh_token: {self.refresh_token}, ' \
               # f'refresh_token_expiry: {self.refresh_token_expiry}'

