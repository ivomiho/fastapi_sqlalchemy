#Me permite usar varias rutas por separado, se lo importa de fastapi
from unittest import result
from fastapi import APIRouter, Response, status
from config.db import conn
from models.user import products
from schemas.user import Product
from starlette.status import HTTP_204_NO_CONTENT

#es lo mismo que venia haciendo, en vez de usar app.get, ahora voy a utilizar user.get
user = APIRouter()

@user.get("/products", response_model=list[Product], tags=["Products"])
def get_products():
    return conn.execute(products.select()).fetchall()

@user.post("/products", response_model=Product, tags=["Products"])
def create_products(user: Product):
    new_product = {"name": user.name, "quantity": user.quantity, "price": user.price}
    result = conn.execute(products.insert().values(new_product))
    print(result.lastrowid)
    return conn.execute(products.select().where(products.c.id == result.lastrowid)).first()

@user.get("/products/{id}", response_model=Product, tags=["Products"])
def search_product(id:str):
    return conn.execute(products.select().where(products.c.id == id)).first()

@user.delete("/products/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Products"])
def delete_product(id:str):
    conn.execute(products.delete().where(products.c.id == id))
    return Response(status_code=HTTP_204_NO_CONTENT)

@user.put("/products/{id}", response_model=Product, tags=["Products"])
def update_product(id:str, user:Product):
    conn.execute(products.update().values(name=user.name, quantity=user.quantity, price=user.price).where(products.c.id == id))
    return conn.execute(products.select().where(products.c.id == id)).first()



    
    

    
    


