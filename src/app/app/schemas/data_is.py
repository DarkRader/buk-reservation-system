"""
DTO schemes for Data from IS.
"""
from typing import Optional
from pydantic import BaseModel, Field


class Organization(BaseModel):
    """Represents an organization."""
    name: Optional[str]
    note: Optional[str]


class UserIS(BaseModel):
    """Represents a user in the IS."""
    country: str
    created_at: str
    email: str
    first_name: str
    id: int
    im: Optional[str]
    note: Optional[str]
    organization: Optional[Organization]
    phone: Optional[str]
    phone_vpn: Optional[str]
    photo_file: Optional[str]
    photo_file_small: Optional[str]
    state: str
    surname: str
    ui_language: Optional[str]
    ui_skin: str
    username: str
    usertype: str


class Service(BaseModel):
    """Represents a service."""
    alias: str
    name: str
    note: Optional[str]
    servicetype: str
    web: str


class ServiceValidity(BaseModel):
    """Represents a service validity."""
    from_: Optional[str] = Field(None, alias='from')
    to: Optional[str]
    note: Optional[str]
    service: Service
    usetype: str


class ServiceList(BaseModel):
    """Represents a list user services."""
    services: list[ServiceValidity]


class LimitObject(BaseModel):
    """Represents a limit object."""
    id: int
    name: str
    alias: Optional[str] = None
    note: Optional[str] = None
    # description: Optional[str]


class Role(BaseModel):
    """Represents a role."""
    role: str
    name: str
    description: str
    limit: str
    limit_objects: list[LimitObject]


class RoleList(BaseModel):
    """Represents a list user roles."""
    roles: list[Role]


class Zone(BaseModel):
    """Represents a zone."""
    alias: Optional[str]
    id: int
    name: str
    note: str


class Room(BaseModel):
    """Represents a room in the IS."""
    door_number: str
    floor: int
    id: int
    name: Optional[str]
    zone: Zone


class InformationFromIS(BaseModel):
    """Represents all information about user from IS."""
    user: UserIS
    room: Room
    services: list[ServiceValidity]
