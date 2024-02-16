from fastapi import FastAPI
from sqlalchemy import create_engine, MetaData
from com.Emp_data.common.constant import database, port, password, host
from sqlalchemy.orm import sessionmaker
# from com.Emp_data.database.model import Base

SQL_DATABASE_URL = "mysql+pymysql://root:root1234@localhost:3306/emp"
engine = create_engine(SQL_DATABASE_URL, echo=False)
conn = engine.connect()

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)


















# def connect_database():
#     try:
#
#         meta = MetaData()
#
#
#         session = Session()
#
#     except Exception as e:
#         print("Error connecting to the database:", str(e))
#
#
# connect_database()

# def close_session():
#     try:
#         session.close()
#         conn.close()
#         engine.dispose()
#     except Exception as e:
#         session.rollback()
#         print("error in close database", str(e))

# print(conn)
