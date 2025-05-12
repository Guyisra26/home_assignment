from pydantic import BaseModel, Field
from enum import Enum
from typing import Any


class StatusEnum(str, Enum):
    active = "active"
    inactive = "inactive"


class User(BaseModel):
    status: StatusEnum = Field(..., description="Active/inactive")


class Partner(BaseModel):
    data: Any = Field(..., description="Any JSON-compatible data")
