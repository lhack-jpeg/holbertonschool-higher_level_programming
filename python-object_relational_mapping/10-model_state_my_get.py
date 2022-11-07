#!/usr/bin/python3
'''Script lists that searches for state  using SQLalchemy.'''


from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    '''Entry into script. If table is empty print nothing'''
    user_input = argv[4]
    user_input = user_input.split(';')
    user_input = user_input[0].replace('\'', '').replace("\"", "")
    engine = create_engine(
        f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}",
        pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    obj = session.query(State).filter(State.name == user_input).first()
    if obj:
        print(obj.id)
    else:
        print('Not found')
