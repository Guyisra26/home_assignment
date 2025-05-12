import pytest
import tempfile
import shutil
from pathlib import Path
from uuid import UUID, uuid4
from db.database_client import DatabaseClient
from models.schema import Partner


@pytest.fixture
def temp_partners_db():
    tmp_dir = Path(tempfile.mkdtemp())
    db = DatabaseClient(tmp_dir / "partners.json")
    yield db
    shutil.rmtree(tmp_dir)


def test_put_and_get_partner(temp_partners_db):
    partner_id = uuid4()
    partner = Partner(data={"name": "Google Inc."})

    temp_partners_db.put(partner.model_dump(), partner_id)

    result = temp_partners_db.get(partner_id)
    assert result is not None
    assert result["data"]["name"] == "Google Inc."


def test_get_all_partners(temp_partners_db):
    partner_id = uuid4()
    partner = Partner(data={"name": "Google Inc."})
    temp_partners_db.put(partner.model_dump(), partner_id)
    partner_id2 = uuid4()
    partner2 = Partner(data={"name": "Microsoft Corp."})
    temp_partners_db.put(partner2.model_dump(), partner_id2)
    all_partners = temp_partners_db.get()
    assert isinstance(all_partners, dict)
    assert len(all_partners) == 2


def test_update_partner_data(temp_partners_db):
    partner_id = uuid4()
    temp_partners_db.put({"name": "Google Inc."}, partner_id)
    updated_data = {"name": "Google LLC", "address": "Mountain View, CA"}
    temp_partners_db.put(updated_data, partner_id)
    updated_partner = temp_partners_db.get(partner_id)
    assert updated_partner is not None
    assert updated_partner["address"] == "Mountain View, CA"


def test_delete_partner(temp_partners_db):
    partner_id = uuid4()
    partner = Partner(data={"name": "Google Inc."})
    temp_partners_db.put(partner.model_dump(), partner_id)
    assert temp_partners_db.get(partner_id) is not None
    delete_partner = temp_partners_db.delete(partner_id)
    assert delete_partner is True
    assert temp_partners_db.get(partner_id) is None


@pytest.fixture
def temp_user_db():
    tmp_dir = Path(tempfile.mkdtemp())
    db = DatabaseClient(tmp_dir / "users.json")
    yield db
    shutil.rmtree(tmp_dir)


def test_put_and_get_user(temp_user_db):
    user_data = {"id": str(uuid4()), "status": "active"}
    user_id = temp_user_db.put(user_data, UUID(user_data["id"]))
    result = temp_user_db.get(UUID(user_id))
    assert result is not None
    assert result["status"] == "active"


def test_get_all_users(temp_user_db):
    temp_user_db.put({"id": str(uuid4()), "status": "active"})
    temp_user_db.put({"id": str(uuid4()), "status": "inactive"})
    result = temp_user_db.get()
    assert isinstance(result, dict)
    assert len(result) == 2


def test_update_user_status(temp_user_db):
    # create a user
    user_id = uuid4()
    temp_user_db.put({"status": "active"}, user_id)

    # update status
    updated_data = {"status": "inactive"}
    temp_user_db.put(updated_data, user_id)

    # retrieve and check
    user = temp_user_db.get(user_id)
    assert user is not None
    assert user["status"] == "inactive"


def test_delete_user(temp_user_db):
    user_id = uuid4()
    temp_user_db.put({"id": str(user_id), "status": "active"}, user_id)
    assert temp_user_db.delete(user_id)
    assert temp_user_db.get(user_id) is None


def test_delete_non_existing_user(temp_user_db):
    fake_id = uuid4()
    assert not temp_user_db.delete(fake_id)
