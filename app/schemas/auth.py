from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


# Auth Schemas
class Login(BaseModel):
    email: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str