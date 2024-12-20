from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from app.cruds.user import UserCrud
from app.database import get_db
from app.schemas.user import UserDTO

router = APIRouter()


@router.post("/login", status_code=201)
async def add_user(dto: UserDTO, db: Session = Depends(get_db)):
    print(dto)
    user_token_dto = UserCrud(db).add_user(request_user=dto).dict()
    return JSONResponse(status_code=200,
                        content=dict(
                            msg=jsonable_encoder(user_token_dto)
                        ))


@router.get("/get", status_code=201)
async def get_user(db: Session = Depends(get_db)):
    return JSONResponse(status_code=200,
                        content=dict(
                            msg=UserCrud(db).get_user()
                        ))




