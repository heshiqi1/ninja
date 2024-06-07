from ninja import Schema
from typing import Optional


class MockSchema(Schema):
    name: str
    description: Optional[str] = None
    method: Optional[str] = None
    path: Optional[str] = None
    res: dict


class ResponSchema(Schema):
    body: Optional[list] = []
    msg: Optional[str] = None

