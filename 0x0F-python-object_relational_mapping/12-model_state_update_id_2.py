#!/usr/bin/python3
"""
Script that adds the State object “Louisiana”
to the database hbtn_0e_6_usa.
"""
if __name__ == "__main__":
    try:
        import sys
        from model_state import Base, State
        from sqlalchemy import create_engine
        from sqlalchemy.orm import Session
        """This script should take 3 arguments: mysql username, mysql password
        and database name"""
        eng = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                            format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)

        Base.metadata.create_all(eng)
        session = Session(eng)
        state_to_update = session.query(State).filter(State.id == 2).first()
        state_to_update.name = 'New Mexico'
        session.commit()
        session.close()
    except:
        print("Can't connect to database")
