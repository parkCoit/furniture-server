from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from app.cruds.furniture import FurnitureCrud
from app.database import get_db
from app.schemas.furniture import FurnitureDTO

router = APIRouter()


@router.post("/", status_code=201)
async def create_furniture(dto: FurnitureDTO, db: Session = Depends(get_db)):
    return JSONResponse(status_code=200,
                        content=dict(
                            msg=FurnitureCrud(db).create_furniture(request=dto)
                        ))


@router.get("/{furniture_id}", status_code=201)
async def read_furniture(furniture_id: int, db: Session = Depends(get_db)):
    return JSONResponse(status_code=200,
                        content=dict(
                            msg=FurnitureCrud(db).read_furniture(furniture_id=furniture_id)
                        ))


@router.put("/{furniture_id}", status_code=201)
async def update_furniture(dto: FurnitureDTO, furniture_id: int, db: Session = Depends(get_db)):
    return JSONResponse(status_code=200,
                        content=dict(
                            msg=FurnitureCrud(db).update_furniture(furniture_id=furniture_id, request=dto)
                        ))


@router.delete("/{furniture_id}", status_code=201)
async def delete_furniture(furniture_id: int, db: Session = Depends(get_db)):
    return JSONResponse(status_code=200,
                        content=dict(
                            msg=FurnitureCrud(db).delete_furniture(furniture_id=furniture_id)
                        ))


