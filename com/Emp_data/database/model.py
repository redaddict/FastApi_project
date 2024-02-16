from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from com.Emp_data.database.db import engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String)


class Company(Base):
    __tablename__ = 'companies'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    employees = relationship("Employee", back_populates="company")


class Client(Base):
    __tablename__ = 'clients'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    email = Column(String(100))
    phone = Column(String(100))
    user_id = Column(Integer, ForeignKey('users.id'))
    company_id = Column(Integer, ForeignKey('companies.id'))


class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    company_id = Column(Integer, ForeignKey('companies.id'))
    company = relationship("Company", back_populates="employees")


#
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import Column, Integer, Boolean, String, ForeignKey
# from sqlalchemy.orm import relationship
#
# Base = declarative_base()
#
#
# # class EmpInfo(Base):
# #     __tablename__ = "Employee_Tables"
# #
# #     Id = Column(INTEGER, primary_key=True,autoincrement = True, index=True)
# #     Emp_name = Column(VARCHAR(50))
# #     Emp_salary = Column(INTEGER)
#
#
# class User(Base):
#     __tablename__ = 'users'
#     id = Column(Integer, primary_key=True, index=True)
#     username = Column(String(100), unique=True, index=True)
#
#
# class Company(Base):
#     __tablename__ = 'companies'
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String(100))
#
#
# class Client(Base):
#     __tablename__ = 'clients'
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String(100))
#     email = Column(String(100))
#     phone = Column(String(100))
#     user_id = Column(Integer, ForeignKey('users.id'))
#     company_id = Column(Integer, ForeignKey('companies.id'))
#     user = relationship("User", back_populates="clients")
#     company = relationship("Company", back_populates="clients")
#
#
# class ClientUser(Base):
#     __tablename__ = 'client_users'
#     id = Column(Integer, primary_key=True, index=True)
#     client_id = Column(Integer, ForeignKey('clients.id'))
#     user_id = Column(Integer, ForeignKey('users.id'))
#     created_at = Column(String(100))
#     updated_at = Column(String(100))
#     deleted_at = Column(String(100))
#     active = Column(Boolean)
#     client = relationship("Client", back_populates="client_users")
#     user = relationship("User", back_populates="client_users")
#
#
Base.metadata.create_all(engine)
