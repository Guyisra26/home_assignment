from tkinter.ttk import Label
from wsgiref.simple_server import demo_app

from fastapi import FastAPI, Query, HTTPException

from models import User, Partner, StatusEnum, UpdateUserStatus
from storage import load_users, save_users, load_partners, save_partners

app = FastAPI()

users_db = load_users()
partners_db = load_partners()


@app.get("/users")
def get_users():
    return list(users_db)


@app.get("/users/by-id")
def get_user(id: int = Query(..., description="User ID")):
    user = users_db.get(id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@app.get("/users/exists")
def user_exists(id: int = Query(..., description="User ID to check")):
    return {"exists": id in users_db}


@app.post("/users")
def create_user(user: User):
    if user.id in users_db:
        raise HTTPException(status_code=400, detail="User already exsists")
    users_db[user.id] = user
    save_users(users_db)
    return user


@app.put("/users")
def update_user(user: User):
    if user.id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    users_db[user.id] = user
    save_users(users_db)
    return user


@app.patch("/users/status")
def update_user_status(id: int = Query(...), status_data: UpdateUserStatus = ...):
    user = users_db.get(id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user.status = status_data.status
    users_db[id] = user
    save_users(users_db)
    return user


@app.delete("/users")
def delete_user(id: int = Query(..., description="User ID to delete")):
    if id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    deleted_user = users_db.pop(id)
    save_users(users_db)
    return deleted_user


@app.get("/partners")
def get_partners():
    return list(partners_db.values())


@app.get("/partners/by-id")
def get_partner(id: int = Query(..., description="Partner ID")):
    partner = partners_db.get(id)
    if not partner:
        raise HTTPException(status_code=404, detail="Partner not found")
    return partner


@app.get("/partners/exists")
def partner_exists(id: int = Query(..., description="Check if partner exists")):
    return {"exists": id in partners_db}


@app.post("/partners")
def create_partner(partner: Partner):
    if partner.id in partners_db:
        raise HTTPException(status_code=400, detail="Partner already exists")
    partners_db[partner.id] = partner
    save_partners(partners_db)
    return partner


@app.put("/partners")
def update_partner(partner: Partner):
    if partner.id not in partners_db:
        raise HTTPException(status_code=404, detail="Partner not found")
    partners_db[partner.id] = partner
    save_partners(partners_db)
    return partner


@app.delete("/partners")
def delete_partner(id: int = Query(..., description="Partner ID to delete")):
    if id not in partners_db:
        raise HTTPException(status_code=404, detail="Partner not found")
    deleted_partner = partners_db.pop(id)
    save_partners(partners_db)
    return deleted_partner
