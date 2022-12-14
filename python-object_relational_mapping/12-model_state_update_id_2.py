#!/usr/bin/python3
'''Script changes id = 2 to New Meixco to the Database.'''

from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}",
        pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state_change = session.query(State).filter(State.id == 2).first()
    state_change.name = 'New Mexico'
    session.commit()
    session.close()
