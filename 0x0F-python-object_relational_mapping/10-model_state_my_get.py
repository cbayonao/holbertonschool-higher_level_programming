#!/usr/bin/python3
"""
Script that prints the State object with the name passed
as argument from the database hbtn_0e_6_usa.
"""
if __name__ == "__main__":
    try:
        import sys
        from model_state import Base, State
        from sqlalchemy import create_engine
        from sqlalchemy.orm import Session
        """This script should take 3 arguments: mysql username, mysql password
        and database name"""
        en = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
        Base.metadata.create_all(en)
        session = Session(en)
        state = session.query(State).filter(State.name == sys.argv[4]).first()
        if state:
            print(state.id)
        else:
            print("Not found")
    except:
        print("Can't connect to database")
