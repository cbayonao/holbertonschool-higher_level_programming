#!/usr/bin/python3
"""
Script that lists all City objects from
the database hbtn_0e_101_usa.
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

    query = session.query(State, City).join(City).order_by(City.id)
    for state, city in query.all():
        print("{}: {} -> {}".format(city.id, city.name, state.name))
