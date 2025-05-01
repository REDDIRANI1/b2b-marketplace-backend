from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Optional
from .. import crud, schemas
from ..database import get_db

router = APIRouter(
    prefix="/manufacturers",
    tags=["Manufacturers"]
)

@router.get("/", response_model=list[schemas.Manufacturer])
def read_manufacturers(
    local_kw: Optional[str] = None,
    limit: int = 5,
    offset: int = 0,
    db: Session = Depends(get_db)
):
    return crud.get_manufacturers(db, local_kw, limit, offset)

@router.get("/{manufacturer_id}", response_model=schemas.Manufacturer)
def read_manufacturer(
    manufacturer_id: int,
    db: Session = Depends(get_db)
):
    return crud.get_manufacturer(db, manufacturer_id)

@router.post("/", response_model=schemas.Manufacturer)
def create_manufacturer(
    data: schemas.ManufacturerCreate,
    db: Session = Depends(get_db)
):
    return crud.create_manufacturer(db, data)

@router.put("/{manufacturer_id}", response_model=schemas.Manufacturer)
def update_manufacturer(
    manufacturer_id: int,
    data: schemas.ManufacturerUpdate,
    db: Session = Depends(get_db)
):
    manufacturer = crud.update_manufacturer(db, manufacturer_id, data)
    if not manufacturer:
        raise HTTPException(status_code=404, detail="Manufacturer not found")
    return manufacturer

@router.delete("/{manufacturer_id}")
def delete_manufacturer(
    manufacturer_id: int,
    db: Session = Depends(get_db)
):
    deleted = crud.delete_manufacturer(db, manufacturer_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Manufacturer not found")
    return {"message": "Manufacturer deleted"}
