from pathlib import Path
from db.database_client import DatabaseClient


DATA_DIR = Path(__file__).parent / "data"

users_db = DatabaseClient(DATA_DIR / "users.json")
partners_db = DatabaseClient(DATA_DIR / "partners.json")
