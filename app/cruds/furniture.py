from abc import ABC

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.bases.furniture import FurnitureBase
from app.entities.furniture import Furniture
from app.schemas.furniture import FurnitureDTO


class FurnitureCrud(FurnitureBase, ABC):
    def __init__(self, db: Session):
        self.db: Session = db

    def create_furniture(self, request: FurnitureDTO):
        print(request)
        db_furniture = Furniture(**request.dict())
        self.db.add(db_furniture)
        self.db.commit()
        self.db.refresh(db_furniture)
        return "가구 생성 완료!"

    def read_furniture(self, furniture_id: int):
        db_furniture = self.db.query(Furniture).filter(Furniture.id == furniture_id).first()
        if db_furniture is None:
            raise HTTPException(status_code=404, detail="Furniture not found")
        return db_furniture

    def update_furniture(self, furniture_id: int, request: FurnitureDTO):
        db_furniture = self.db.query(Furniture).filter(Furniture.id == furniture_id).first()
        if db_furniture is None:
            raise HTTPException(status_code=404, detail="Furniture not found")

        db_furniture.name = request.name
        db_furniture.color = request.color
        db_furniture.material = request.material
        db_furniture.size = request.size
        db_furniture.style = request.style

        self.db.commit()
        self.db.refresh(db_furniture)
        return db_furniture

    def delete_furniture(self, furniture_id: int):
        db_furniture = self.db.query(Furniture).filter(Furniture.id == furniture_id).first()
        if db_furniture is None:
            raise HTTPException(status_code=404, detail="Furniture not found")

        self.db.delete(db_furniture)
        self.db.commit()
        return db_furniture
