from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class Customers(Base):

    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)
    email = Column(String)


class Presidents(Base):

    __tablename__ = 'presidents'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    companies = relationship('Companies', uselist=False, back_populates='president') # 1対多で紐づける際に自動でデータを取得

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


engine = create_engine('sqlite:///data2.sqlite', echo=True)


Session = sessionmaker(bind=engine)
session = Session()