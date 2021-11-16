# 01_create.py
from sqlalchemy import (
    create_engine, MetaData, Column, Table,
    Integer, String
)


engine = create_engine('sqlite:///data.sqlite', echo=True)

meta = MetaData()
students = Table(
    'students', meta,
    Column('id', Integer, primary_key=True),
    Column('first_name', String),
    Column('last_name', String)
)

addresses = Table(
    'addresses', meta,
    Column('id', Integer, primary_key=True),
    Column('student_id', Integer),
    Column('postal_address', String),
    Column('email_address', String)
)
