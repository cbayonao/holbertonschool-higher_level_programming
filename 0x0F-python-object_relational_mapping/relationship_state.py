#!/usr/bin/python3
"""
File that contains the class definition of a State and
an instance Base = declarative_base()
"""
from sqlalchemy.orm import relationship
from relationship_city import City, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


class State(Base):
    """Class State"""
    __tablename__ = 'states'
    id = Column(Integer, nullable=False, unique=True, autoincrement=True,
                primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref='states')
