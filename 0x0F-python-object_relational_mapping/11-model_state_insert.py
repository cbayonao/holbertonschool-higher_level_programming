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
        en = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
        session = Session(en)
        state_to_add = State(name='Louisiana')
        session.add(state_to_add)
        session.commit()
        print(state_to_add.id)
        session.close()
    except:
        print("Can't connect to database")
