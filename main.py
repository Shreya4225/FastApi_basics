from fastapi import FastAPI
from models import Product

app = FastAPI()

@app.get("/home")
def abc():
    return "hello shreya"

products = [
    Product(id=1, name="phone", description= "a smartphone", price =699.99, quantity = 50),
    Product(id=2, name="laptop", description= "a laptop", price =699.99, quantity = 50),
    Product(id=3, name="pen", description= "a pen", price =699.99, quantity = 50),
    Product(id=4, name="table", description= "a table", price =699.99, quantity = 50),
]

@app.get("/products")
def get_all_products():
    return products

@app.get("/product/{id}")
def get_product_by_id(id:int):
    for i in products:
        if i.id == id:
            return i
        
    return "product not found"

@app.post("/product")
def add_product(product:Product): #product:Product -> passing the same format of products for accepting the data input
    products.append(product)
    return product

@app.put("/product")
def update_product(id: int, product: Product):
    for i in range(len(products)):
        if products[i]==id:
            products[i]=product
            return "product updated successfully" 
        return "no product found"