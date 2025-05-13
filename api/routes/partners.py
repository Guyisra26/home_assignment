from http import HTTPStatus

from fastapi.responses import JSONResponse

from fastapi import APIRouter, HTTPException, Query
from typing import Optional
from models.schema import Partner
from init_services import partners_db
from uuid import UUID
from fastapi import Body

router = APIRouter(prefix="/partners", tags=["partners"])


@router.get("")
def get_all_partners():
    response = partners_db.get()
    if response is None:
        raise HTTPException(status_code=404, detail="Partner not found")
    return JSONResponse(status_code=HTTPStatus.OK, content=response)


@router.get("/{id}")
def get_partner_by_id(id: UUID):
    response = partners_db.get(id)
    if response is None:
        raise HTTPException(status_code=404, detail="Partner not found")
    return JSONResponse(status_code=HTTPStatus.OK, content=response)


@router.post("")
def create_partner(partner: Partner = Body(...)):
    partner_id = partners_db.put(partner.model_dump(mode="json"))
    return JSONResponse(status_code=HTTPStatus.OK, content=partner_id)


@router.put("/{id}")
def update_partner(id: UUID, partner: Partner = Body(...)):
    existing_partner = partners_db.get(id)
    if not existing_partner:
        raise HTTPException(status_code=404, detail="Partner not found")
    partner_id = partners_db.put(partner.model_dump(mode="json"), id)
    return JSONResponse(status_code=HTTPStatus.OK, content=partner_id)


@router.delete("/{id}")
def delete_partner(id: UUID):
    deleted_partner = partners_db.get(id)
    if deleted_partner is None:
        raise HTTPException(status_code=404, detail="Partner not Found")
    response = partners_db.delete(id)
    return JSONResponse(status_code=HTTPStatus.OK, content=response)
