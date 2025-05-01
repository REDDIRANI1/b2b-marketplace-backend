from typing import List, Optional
from pydantic import BaseModel

class ProductBase(BaseModel):
    name: str
    price: float

class Product(ProductBase):
    id: int
    class Config:
        orm_mode = True

class ManufacturerBase(BaseModel):
    name: str
    category: str
    city: str

class ManufacturerCreate(ManufacturerBase):
    pass

class ManufacturerUpdate(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    city: Optional[str] = None

class Manufacturer(ManufacturerBase):
    id: int
    products: List[Product] = []
    class Config:
        orm_mode = True
