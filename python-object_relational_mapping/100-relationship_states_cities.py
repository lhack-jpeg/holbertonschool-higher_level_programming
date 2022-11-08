#!/usr/bin/python3
'''Script creates a state class with the update constructor.'''

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from relationship_state import Base, State
from relationship_city import City


if __name__ == "__main__":
    '''Entry into script.'''
    engine = create_engine(
        f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}",
        pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    s1 = State(name="California")
    c1 = City(name="San Francsico", state=State(name="California"))
    session.add(c1)
    session.commit()
    session.close()
