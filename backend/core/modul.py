from pydantic import BaseModel, EmailStr
from typing import List

class sign_up_reset(BaseModel):
    email: EmailStr
    username: str
    password: str
    driver:bool

class caller(BaseModel):
    origin: str
    destination:str

class ConfirmUserData(BaseModel):
    destination: str
    origins: str
    users: List[str]
    _id: List[str]


class ConfirmDataModul(BaseModel):
    data: List[ConfirmUserData]
