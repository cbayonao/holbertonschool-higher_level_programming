#!/usr/bin/python3
"""
Script that lists all State objects from the database hbtn_0e_6_usa.
"""
if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    """This script should take 3 arguments: mysql username, mysql password
    and database name"""
    en = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1],
                       sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(en)
    session = Session(en)
    """Results must be sorted in ascending order by states.id"""
    for state in session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
