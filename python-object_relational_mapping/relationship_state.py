#!/usr/bin/python3
'''Module contains the constructor for the State class.'''


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from relationship_city import Base, City


class State(Base):
    '''Creates the state class'''
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship(
        "City",
        backref="state",
        cascade="all, delete",
    )
