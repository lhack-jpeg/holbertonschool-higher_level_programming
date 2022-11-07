#!/usr/bin/python3
'''Script lists first  state using SQLalchemy.'''


from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    '''Entry into script. If table is empty print nothing'''
    engine = create_engine(
        f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}",
        pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    instance = session.query(State).first()
    if not instance:
        print()
    else:
        print(f'{instance.id}: {instance.name}')
