from sqlalchemy import (
    create_engine, MetaData, Column, Table,
    Integer, String, ForeignKey
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine('sqlite:///data2.sqlite', echo=True)
Base = declarative_base()

class Presidents(Base):

    __tablename__ = 'presidents'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    companies = relationship('Companies', back_populates='president') # 1対多で紐づける際に自動でデータを取得

class Companies(Base):

    __tablename__ = 'companies'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    president_id = Column(Integer, ForeignKey('presidents.id'))
    president = relationship('Presidents', back_populates='companies')
    employees = relationship('Employees', back_populates='company')


class Employees(Base):

    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    company_id = Column(Integer, ForeignKey('companies.id'))
    company = relationship('Companies', back_populates='employees')

Base.metadata.create_all(engine)