from pydantic import BaseModel, Field
from enum import Enum
from typing import Any


class StatusEnum(str, Enum):
    active = "active"
    inactive = "inactive"


class UpdateUserStatus(BaseModel):
    status: StatusEnum


class User(BaseModel):
    id: int
    status: StatusEnum = Field(..., description="Active/inactive")


class Partner(BaseModel):
    id: int
    data: Any = Field(..., description="Any JSON-compatible data")
