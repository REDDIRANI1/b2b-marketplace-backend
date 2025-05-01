from sqlalchemy.orm import Session
from . import models, database

def seed_data():
    db: Session = database.SessionLocal()

    if db.query(models.Manufacturer).first():
        print("Data already seeded.")
        return

    m1 = models.Manufacturer(name="Apex Textiles", category="Textile", city="Surat")
    m2 = models.Manufacturer(name="GreenChem Labs", category="Chemicals", city="Mumbai")

    m1.products = [
        models.Product(name="Cotton Fabric", price=120.5),
        models.Product(name="Polyester Yarn", price=90.0)
    ]
    m2.products = [
        models.Product(name="Cleaning Agent X", price=450.0),
        models.Product(name="Industrial Solvent Z", price=650.5)
    ]

    db.add_all([m1, m2])
    db.commit()
    db.close()
    print("Database seeded successfully.")

if __name__ == "__main__":
    seed_data()