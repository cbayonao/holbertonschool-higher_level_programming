#!/usr/bin/python3
"""
Script that lists all State objects, and corresponding City
objects, contained in the database hbtn_0e_101_usa.
"""
import sys
from sqlalchemy import (create_engine)
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    en = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                       format(sys.argv[1], sys.argv[2],
                              sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(bind=en)
    Session = sessionmaker()
    Session.configure(bind=en)
    session = Session()

    query = session.query(State).outerjoin(City).order_by(State.id, City.id)
    for state in query.all():
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))
