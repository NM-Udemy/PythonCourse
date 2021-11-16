from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String


Base = declarative_base()

class Customers(Base):

    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)
    email = Column(String)


engine = create_engine('sqlite:///data2.sqlite', echo=True)
Base.metadata.create_all(engine)

