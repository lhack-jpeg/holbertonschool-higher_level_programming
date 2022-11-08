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
        State, City).filter(
            State.id == City.state_id).order_by(
                City.state_id, City.id)
    city_list = []
    for row in q:
        city_list.append(row)

    for i in range(len(city_list)):
        try:
            if city_list[i][0].id == city_list[i - 1][0].id:
                pass
            else:
                state = city_list[i][0]
                print(f'{state.id}: {state.name}')
        except IndexError:
            pass
        city = city_list[i][1]
        print(f"\t {city.id}: {city.name}")
