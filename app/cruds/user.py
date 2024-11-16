from uuid import uuid4

import pymysql
from sqlalchemy import exists
from sqlalchemy.orm import Session

from abc import ABC
from app.bases.user import UserBase
from app.models.user import User
from app.schemas.user import UserDTO
from app.services.user import UserServices

pymysql.install_as_MySQLdb()


class UserCrud(UserBase, ABC):

    def __init__(self, db: Session):
        self.db: Session = db

    def add_user(self, request_user: UserDTO):
        code = request_user.code
        get_token = UserServices().get_token(code)
        if get_token == 'invalid_grant':
            return {'data': 'not found token'}
        else:
            kakao_user = UserServices().get_kakao_user(get_token)
            access_token = UserServices().get_jwt(kakao_user)
            print(access_token)
            if self.find_kakao_exists(kakao_user['kakao_id']) is False:
                return ''
            else:
                return ''

    def find_kakao_exists(self, kakao_id: str):
        return self.db.query(exists().where(User.kakao_id == kakao_id)).scalar()

    def get_user(self):
        user = self.db.query(User).all()
        user_ls = [{"kakaoid": user[i].userid,
                    "email": user[i].password,
                    "token": user[i].token} for i in range(len(user))]
        return user_ls
