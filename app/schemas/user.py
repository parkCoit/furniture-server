from typing import Optional

from pydantic import BaseModel


class UserVo(BaseModel):
    class Config:
        arbitrary_types_allowed = True


class UserDTO(UserVo):
    userid: Optional[str]
    password: Optional[str]
    token: Optional[str]

    def __str__(self):
        return f'userid: {self.userid},' \
               f'password: {self.password}' \
               f'token: {self.token},'
