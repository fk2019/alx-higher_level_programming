#!/usr/bin/python3
"""
   Updte name of State object with id=2
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine, func
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3], pool_pre_ping=True))
    Base.metadata.create_all(engine)
    session = Session(engine)
    name = "New Mexico"
    obj_id = 2
    state = session.query(State).filter(
        (State.id) == obj_id).first()
    if state:
        state.name = name
        session.commit()
    else:
        print("Not found")
    session.close()
