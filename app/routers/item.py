from fastapi import APIRouter
from typing import Union

router = APIRouter()


@router.get("/{item_id}")
def item_router(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
