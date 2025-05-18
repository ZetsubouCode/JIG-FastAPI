from fastapi import FastAPI
from .database import Base, engine
from .routers import film  # add film here

app = FastAPI(title="FastAPI + SQL Server")

# Create all tables (if they don't already exist)
Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(film.router)        # <— here
