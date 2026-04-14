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
    Product(id=4,name="Headphone",description= "Gaming Headphone",price=77.77,quantity=30)
]

@app.get("/products")
def get_all_products():
    return products