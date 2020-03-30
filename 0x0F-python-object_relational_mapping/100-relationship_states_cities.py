#!/usr/bin/python3
"""
"""
import sys
from sqlalchemy import (create_engine)
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    en = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(bind = en)
    Session = sessionmaker()
    Session.configure(bind=en)
    session = Session()
    n_state = State(name="California")
    n_city = City(name="San Francisco")
    n_state.cities.append(n_city)
    session.add(n_state)
    session.add(n_city)
    session.commit()