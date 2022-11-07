#!/usr/bin/python3
'''Script prints all the cities in the database.'''

from model_state import Base, State
from model_city import City
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    '''Entry Point to script'''
    engine = create_engine(
        f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}",
        pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    instances = session.query(
        City, State).filter(City.state_id == State.id).order_by(City.id)
    for city, state in instances:
        print(f'{state.name}: ({city.id}) {city.name}')
    session.close()
