from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from ..database import SessionLocal
from ..models import Film
from ..schemas import FilmCreate, FilmOut, FilmUpdate

router = APIRouter(prefix="/films", tags=["films"])

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[FilmOut])
def read_films(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return (
        db.query(Film)
          .order_by(Film.rowid)          # ← **new**
          .offset(skip)
          .limit(limit)
          .all()
    )

@router.get("/{film_id}", response_model=FilmOut)
def read_film(film_id: int, db: Session = Depends(get_db)):
    film = db.query(Film).filter(Film.rowid == film_id).first()
    if not film:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Film not found")
    return film

@router.post("/", response_model=FilmOut, status_code=status.HTTP_201_CREATED)
def create_film(film_in: FilmCreate, db: Session = Depends(get_db)):
    film = Film(**film_in.dict())
    db.add(film)
    db.commit()
    db.refresh(film)
    return film

@router.put("/{film_id}", response_model=FilmOut)
def update_film(film_id: int, film_in: FilmUpdate, db: Session = Depends(get_db)):
    film = db.query(Film).filter(Film.rowid == film_id).first()
    if not film:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Film not found")
    for field, value in film_in.dict(exclude_unset=True).items():
        setattr(film, field, value)
    db.commit()
    db.refresh(film)
    return film

@router.delete("/{film_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_film(film_id: int, db: Session = Depends(get_db)):
    film = db.query(Film).filter(Film.rowid == film_id).first()
    if not film:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Film not found")
    db.delete(film)
    db.commit()
    return
