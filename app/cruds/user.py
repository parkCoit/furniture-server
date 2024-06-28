from uuid import uuid4

import pymysql
from sqlalchemy.orm import Session

from abc import ABC
from app.bases.user import UserBase
from app.entities.user import User
from app.schemas.user import UserDTO

pymysql.install_as_MySQLdb()


class UserCrud(UserBase, ABC):

    def __init__(self, db: Session):
        self.db: Session = db

    def add_user(self, request_user: UserDTO):
        user = User(**request_user.dict())
        print(f"user :::: {user}"
              f"userid ::: {user.userid}")
        db_user = User(userid=user.userid, password=user.password, token=user.token)
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return "회원 가입완료!"

    def get_user(self):
        user = self.db.query(User).all()
        user_ls = [{"userid" : user[i].userid,
                    "password" : user[i].password,
                    "token" : user[i].token} for i in range(len(user))]
        return user_ls
