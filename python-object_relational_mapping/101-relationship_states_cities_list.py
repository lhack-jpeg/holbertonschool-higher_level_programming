#!/usr/bin/python3
'''Script Lists out the state and the cities attached to them.'''

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


if __name__ == "__main__":
    engine = create_engine(
        f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}",
        pool_pre_ping=True,
        )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    q = session.query(
        State).order_by(State.id).all()
    for row in q:
        print(f'{row.id}: {row.name}')
        for city in row.cities:
            print(f'\t{city.id}: {city.name}')
