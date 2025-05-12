from uuid import UUID

from main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_create_user():
    response = client.post("/users", json={"status": "active"})
    user_id = UUID(response.json())
    exists_user = client.get(f"/users?id={user_id}")
    assert response.status_code == 200
    assert exists_user.status_code == 200


def test_create_user_missing_status():
    response = client.post("/users", json={})
    assert response.status_code == 422


def test_create_user_invalid_status():
    response = client.post("/users", json={"status": "invalid_status"})
    assert response.status_code == 422


def test_get_users():
    response = client.get("/users")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert len(response.json()) > 0


def test_get_users_invalid_id():
    response = client.get("/users?id=4309t4p-27d1-4511-b6da-ee40b1b14f07")
    assert response.status_code == 422


def test_update_user():
    user_res = client.post("/users", json={"status": "active"})
    user_id = user_res.json()
    is_updated = client.put(f"/users?id={user_id}", json={"status": "inactive"})
    updated_user_res = client.get(f"/users?id={user_id}")
    assert user_res.status_code == 200
    assert is_updated.status_code == 200
    assert updated_user_res.json() == {"status": "inactive"}


def test_delete_user():
    new_user = client.post("/users", json={"status": "active"})
    response = client.delete(f"/users?id={new_user.json()}")
    assert response.status_code == 200
    response = client.get(f"/users?id={new_user.json()}")
    assert response.status_code == 404


def test_create_partner():
    response = client.post("/partners", json={"data": {"name": "Google Inc."}})
    partner_id = UUID(response.json())
    exists_partner = client.get(f"/partners?id={partner_id}")
    assert response.status_code == 200
    assert exists_partner.status_code == 200


def test_get_partners():
    response = client.get("/partners")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert len(response.json()) > 0


def test_update_partner():
    partner_res = client.post("/partners", json={"data": {"name": "Amazon Inc."}})
    partner_id = partner_res.json()
    is_updated = client.put(
        f"/partners?id={partner_id}", json={"data": {"name": "Microsoft Inc."}}
    )
    updated_partner_res = client.get(f"/partners?id={partner_id}")
    assert partner_res.status_code == 200
    assert is_updated.status_code == 200
    assert updated_partner_res.json() == {"data": {"name": "Microsoft Inc."}}


def test_delete_partner():
    new_partner = client.post("/partners", json={"data": {"name": "Meta Inc."}})
    response = client.delete(f"/partners?id={new_partner.json()}")
    assert response.status_code == 200
    response = client.get(f"/partners?id={new_partner.json()}")
    assert response.status_code == 404


def test_create_partner_missing_data():
    response = client.post("/partners", json={})
    assert response.status_code == 422
