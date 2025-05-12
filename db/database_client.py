import json
from uuid import UUID, uuid4
from pathlib import Path
from typing import Optional


class DatabaseClient:
    def __init__(self, path: Path):
        self.file_path = path
        self.data = self._load()

    def _load(self):
        if not self.file_path.exists():
            return {}
        with open(self.file_path) as f:
            return json.load(f)

    def _save(self):
        with open(self.file_path, "w") as f:
            json.dump(self.data, f, indent=2)

    def get(self, id: UUID = None) -> Optional[dict]:
        if not id:
            return self.data
        return self.data.get(str(id))

    def put(self, obj: dict, id: UUID = None) -> str:
        id = id or uuid4()
        self.data[str(id)] = obj
        self._save()
        return str(id)

    def delete(self, id: UUID) -> bool:
        if str(id) in self.data:
            self.data.pop(str(id))
            self._save()
            return True
        return False
