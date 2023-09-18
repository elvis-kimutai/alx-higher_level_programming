#!/usr/bin/python3
"""
Write a script that creates the State “California”
with the City “San Francisco” 
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import Base, City
from relationship_state import State

if __name__ == "__main__":

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(argv[1], argv[2], argv[3]),
        pool_pre_ping=True
    )

    Base.metadata.create_all(engine)
    the_session_maker = sessionmaker(bind=engine)
    the_session = the_session_maker()

    the_session.add(City(name="San Francisco", state=State(name="California")))
    the_session.commit()
    the_session.close()
