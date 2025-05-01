from sqlalchemy import or_
from sqlalchemy.orm import Session
from . import models, schemas
from sqlalchemy.exc import SQLAlchemyError

def get_manufacturers(db: Session, local_kw: str = None, limit: int = 5, offset: int = 0):
    try:
        query = db.query(models.Manufacturer)
        
        if local_kw:
            query = query.filter(
                or_(
                    models.Manufacturer.name.ilike(f"%{local_kw}%"),
                    models.Manufacturer.category.ilike(f"%{local_kw}%"),
                    models.Manufacturer.city.ilike(f"%{local_kw}%")
                )
            )
        
        return query.offset(offset).limit(limit).all()

    except SQLAlchemyError as e:
        print(f"SQLAlchemyError: {e}")
        raise Exception(f"An error occurred while querying the manufacturers: {e}")
    except Exception as e:
        print(f"Error: {e}")
        raise Exception(f"An unexpected error occurred: {e}")

def get_manufacturer(db: Session, manufacturer_id: int):
    try:
        return db.query(models.Manufacturer).filter(models.Manufacturer.id == manufacturer_id).first()
    except Exception as e:
        print(f"Error fetching manufacturer: {e}")
        raise

def create_manufacturer(db: Session, data: schemas.ManufacturerCreate):
    try:
        manufacturer = models.Manufacturer(**data.dict())
        db.add(manufacturer)
        db.commit()
        db.refresh(manufacturer)
        return manufacturer
    except Exception as e:
        print(f"Error creating manufacturer: {e}")
        raise

def update_manufacturer(db: Session, manufacturer_id: int, data: schemas.ManufacturerUpdate):
    try:
        manufacturer = db.query(models.Manufacturer).filter(models.Manufacturer.id == manufacturer_id).first()
        if manufacturer:
            for key, value in data.dict(exclude_unset=True).items():
                setattr(manufacturer, key, value)
            db.commit()
            db.refresh(manufacturer)
        return manufacturer
    except Exception as e:
        print(f"Error updating manufacturer: {e}")
        raise

def delete_manufacturer(db: Session, manufacturer_id: int):
    try:
        manufacturer = db.query(models.Manufacturer).filter(models.Manufacturer.id == manufacturer_id).first()
        if manufacturer:
            db.delete(manufacturer)
            db.commit()
        return manufacturer
    except Exception as e:
        print(f"Error deleting manufacturer: {e}")
        raise
