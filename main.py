from itertools import product

from fastapi import FastAPI
from models import Product
app = FastAPI()
@app.get("/")
def greet():
    return "Hello Form FastAPI"

products = [ 
    Product(id=1,name="Phone",description= "Buget Phone",price=99,quantity=10),
    Product(id=2,name="Laptop",description= "Business Laptop",price=668,quantity=110),
    Product(id=3,name="Monitor",description= "Coding Monitor",price=780.69,quantity=20),
    Product(id=4,name="Headphone",description= "Gaming Headphone",price=77.77,quantity=30),
    Product(id=3, name="Headphone", description="Gaming Headphone", price=77.77, quantity=30)
]

@app.get("/products")
def get_all_products():
    return products

@app.get("/product/{id}")
def get_product(id:int):
    for product in products:
        if product.id == id:
            return product

    return "Product not found"

@app.post("/product")
def add_product(productDto: Product):
    products.append(productDto)
    return {"message":"Product added successfully", "product": productDto}

@app.put("/product/{id}")
def update_product(id: int, productDto: Product):
    for i, product in enumerate(products):
       if product.id == id:
           products[i] = productDto
           return {"message":"Product updated successfully", "product": productDto}

    return {"errror":"Product not found"}

@app.delete("/product/{id}")
def delete_product(id: int):
    for i, product in enumerate(products):
        if product.id == id:
            products.pop(i)
            return {"message":"Product deleted successfully"}

    return {"errror":"Product not found"}