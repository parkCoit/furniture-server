from fastapi import FastAPI, APIRouter

from fastapi.middleware.cors import CORSMiddleware
from fastapi_sqlalchemy import DBSessionMiddleware

from .database import init_db
from .env import DB_URL
from .routers.item import router as item_router
from .routers.user import router as user_router
from .routers.furniture import router as furniture_router

router = APIRouter()

router.include_router(item_router, prefix="/item", tags=["item"])
router.include_router(user_router, prefix="/user", tags=["user"])
router.include_router(furniture_router, prefix="/furniture", tags=["furniture"])

app = FastAPI()
origins = ["http://localhost:8000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(router)

app.add_middleware(DBSessionMiddleware, db_url=DB_URL)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.on_event("startup")
async def on_startup():
    try:
        print('Starting database initialization...')
        await init_db()
    except Exception as e:
        print(f"Database initialization failed: {e}")
        raise e
