from http import HTTPStatus
from fastapi.responses import JSONResponse

from fastapi import APIRouter, HTTPException, Query
from models.schema import User
from init_services import users_db
from uuid import UUID

router = APIRouter(prefix="/users", tags=["users"])


@router.get("")
def get_users(id: UUID = None):
    response = users_db.get(id)
    if response is None:
        raise HTTPException(status_code=404, detail="User not found")
    return JSONResponse(status_code=HTTPStatus.OK, content=response)


@router.post("")
def create_user(user: User = ...):
    user_id = users_db.put(user.model_dump(mode="json"))
    return JSONResponse(status_code=HTTPStatus.OK, content=user_id)


@router.put("")
def update_user(id: UUID = Query(...), user: User = ...):
    existing_user = users_db.get(id)
    if not existing_user:
        raise HTTPException(status_code=404, detail="User not found")
    users_db.put(user.model_dump(mode="json"), id)
    return HTTPStatus.OK


@router.delete("")
def delete_user(id: UUID = Query(...)):
    deleted_user = users_db.get(id)
    if deleted_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    response = users_db.delete(id)
    return JSONResponse(status_code=HTTPStatus.OK, content=response)
