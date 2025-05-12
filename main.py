from fastapi import FastAPI
from api.routes import users, partners

app = FastAPI()

app.include_router(users.router)
app.include_router(partners.router)
