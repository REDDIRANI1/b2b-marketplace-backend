from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from .database import Base

class Manufacturer(Base):
    __tablename__ = "manufacturers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    category = Column(String)
    city = Column(String)

    products = relationship("Product", back_populates="manufacturer")

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    price = Column(Float)
    manufacturer_id = Column(Integer, ForeignKey("manufacturers.id"))

    manufacturer = relationship("Manufacturer", back_populates="products")
