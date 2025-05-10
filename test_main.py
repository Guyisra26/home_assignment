from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_create_user():
    response = client.post("/users", json={"id": 999, "status": "active"})
    assert response.status_code == 200
    assert response.json()["id"] == 999
    assert response.json()["status"] == "active"


def test_user_exists():
    response = client.get("/users/exists", params={"id": 999})
    assert response.status_code == 200
    assert response.json()["exists"] is True


def test_get_user_by_id():
    response = client.get("/users/by-id", params={"id": 999})
    assert response.status_code == 200
    assert response.json()["id"] == 999


def test_update_user_status():
    response = client.patch(
        "/users/status", params={"id": 999}, json={"status": "inactive"}
    )
    assert response.status_code == 200
    assert response.json()["status"] == "inactive"


def test_delete_user():
    response = client.delete("/users", params={"id": 999})
    assert response.status_code == 200
    assert response.json()["id"] == 999


def test_user_no_longer_exists():
    response = client.get("/users/exists", params={"id": 999})
    assert response.status_code == 200
    assert response.json()["exists"] is False


def test_create_partner():
    response = client.post("/partners", json={"id": 888, "data": {"name": "test crop"}})
    assert response.status_code == 200
    assert response.json()["id"] == 888
    assert response.json()["data"]["name"] == "test crop"


def test_partner_exists():
    response = client.get("/partners/exists", params={"id": 888})
    assert response.status_code == 200
    assert response.json()["exists"] is True


def test_get_partner_by_id():
    response = client.get("/partners/by-id", params={"id": 888})
    assert response.status_code == 200
    assert response.json()["id"] == 888


def test_update_partner():
    response = client.put(
        "/partners",
        json={"id": 888, "data": {"name": "UpdatedCorp", "industry": "Tech"}},
    )
    assert response.status_code == 200
    assert response.json()["data"]["name"] == "UpdatedCorp"
    assert response.json()["data"]["industry"] == "Tech"


def test_delete_partner():
    response = client.delete("/partners", params={"id": 888})
    assert response.status_code == 200
    assert response.json()["id"] == 888


def test_partner_no_longer_exists():
    response = client.get("/partners/exists", params={"id": 888})
    assert response.status_code == 200
    assert response.json()["exists"] is False
