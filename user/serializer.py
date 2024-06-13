from ninja import Schema
from typing import Optional


class UserSchema(Schema):
    username: str
    password: str
    email: Optional[str] = None


class ResponSchema(Schema):
    body: Optional[list] = []
    msg: Optional[str] = None

