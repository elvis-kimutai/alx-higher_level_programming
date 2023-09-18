#!/usr/bin/python3
"""
script that deletes all State objects with a name containing the letter a 
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(argv[1], argv[2], argv[3]),
        pool_pre_ping=True
    )

    the_session_maker = sessionmaker(bind=engine)
    the_session = the_session_maker()

    states = the_session.query(State).filter(State.name.like('%a%')).all()
    for state in states:
        the_session.delete(state)
    the_session.commit()

    the_session.close()
