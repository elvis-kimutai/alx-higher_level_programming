#!/usr/bin/python3
"""
Write a script that changes the name of a
State object from the database
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
    the_session = my_session_maker()

    state = the_session.query(State).filter_by(id=2).first()
    state.name = "New Mexico"
    the_session.commit()

    the_session.close()
