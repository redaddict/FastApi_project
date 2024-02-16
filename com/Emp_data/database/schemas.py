# from pydantic import BaseModel
# from typing import ClassVar
#
#
# class EmpInfo(BaseModel):
#     Id : int
#     Emp_name : str
#     Emp_salary : int

from pydantic import BaseModel
from typing import List

class User(BaseModel):
    username: str

class Company(BaseModel):
    name: str

class Client(BaseModel):
    name: str
    user: User
    company: Company
    email: str
    phone: str

class ClientUser(BaseModel):
    client: Client
    users: List[User]
    createdAt: str
    updatedAt: str
    deletedAt: str
    active: bool
