#!/usr/bin/python3
"""
Write a script that adds the State object
“Louisiana” to the database
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

    Base.metadata.create_all(engine)

    new_obj = State(name="Louisiana")
    the_session.add(new_obj)
    the_session.commit()
    print(new_obj.id)

    the_session.close()
