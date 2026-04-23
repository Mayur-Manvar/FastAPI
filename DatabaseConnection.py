from itertools import product
from fastapi import FastAPI, Depends
from models import Product
from Database import session, engine
import DatabaseModels
from sqlalchemy.orm import Session

app = FastAPI()

DatabaseModels.Base.metadata.create_all(engine)

@app.get("/")
def greet():
    return "Hello Form FastAPI"

products = [
    Product(id=1,name="Phone",description= "Budget Phone",price=99,quantity=10),
    Product(id=2,name="Laptop",description= "Business Laptop",price=668,quantity=110),
    Product(id=3,name="Monitor",description= "Coding Monitor",price=780.69,quantity=20),
    Product(id=4,name="Headphone",description= "Gaming Headphone",price=77.77,quantity=30)]

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()


def init_database():
    db = session()

    count = db.query(DatabaseModels.Product).count()

    if count == 0:
        for prod in products:
            db.add(DatabaseModels.Product(**prod.model_dump()))

        db.commit()

init_database()


@app.get("/products")
def get_all_products(db: Session = Depends(get_db)):
    db_products = db.query(DatabaseModels.Product).all()
    return db_products

@app.get("/product/{id}")
def get_product(productid: int, db: Session = Depends(get_db)):
    db_product = db.query(DatabaseModels.Product).filter(DatabaseModels.Product.id == productid).first()

    if db_product:
        return db_product

    return "Product not found"

@app.post("/product")
def add_product(product: Product, db: Session = Depends(get_db)):
    db.add(DatabaseModels.Product(**product.model_dump()))
    db.commit()
    return {"message":"Product added successfully.", "product": product}

@app.put("/product/{id}")
def update_product(id: int, product: Product, db: Session = Depends(get_db)):

    db_product = db.query(DatabaseModels.Product).filter(DatabaseModels.Product.id == id).first()
    if db_product:
        db_product.name = product.name
        db_product.description = product.description
        db_product.price = product.price
        db_product.quantity = product.quantity
        db.commit()
        return {"message":"Product updated successfully.", "product": product}
    else:
        return {"error":"Product not found"}

@app.delete("/product/{id}")
def delete_product(id: int, db: Session = Depends(get_db)):
    db_product = db.query(DatabaseModels.Product).filter(DatabaseModels.Product.id == id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
        return {"message":"Product deleted successfully."}
    else:
        return {"error":"Product not found"}