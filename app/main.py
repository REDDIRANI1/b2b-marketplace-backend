from fastapi import FastAPI
from . import models, database
from .routers import manufacturers
from fastapi.middleware.cors import CORSMiddleware
from .routers import manufacturers, auth


models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Your frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(manufacturers.router)
app.include_router(auth.router)
app.include_router(manufacturers.router)
