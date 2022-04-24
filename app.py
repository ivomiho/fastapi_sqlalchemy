from fastapi import FastAPI
from routes.user import user 

app = FastAPI(title="ProductsBD", description="easy way to manipulate products")
app.include_router(user)





