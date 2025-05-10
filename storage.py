import json
from typing import Dict
from models import User, Partner

USERS_FILE = "users.json"
PARTNERS_FILE = "partners.json"


def load_users() -> Dict[int, User]:
    try:
        with open(USERS_FILE, "r") as file:
            data = json.load(file)
            return {int(key): User(**value) for key, value in data.items()}
    except FileNotFoundError:
        return {}


def save_users(users: Dict[int, User]):
    with open(USERS_FILE, "w") as file:
        json.dump(
            {str(key): value.dict() for key, value in users.items()}, file, indent=2
        )


def load_partners() -> Dict[int, Partner]:
    try:
        with open(PARTNERS_FILE, "r") as file:
            data = json.load(file)
            return {int(key): Partner(**value) for key, value in data.items()}
    except FileNotFoundError:
        return {}


def save_partners(partners: Dict[int, Partner]):
    with open(PARTNERS_FILE, "w") as file:
        json.dump(
            {str(key): value.dict() for key, value in partners.items()}, file, indent=2
        )
