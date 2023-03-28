#!/usr/bin/python3
"""
   Print State object with name passed as argument
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
    name = "Louisiana"
    obj = State(name=name)
    session.add(obj)
    session.commit()
    state = session.query(State).filter(
        func.binary(State.name) == name).order_by(State.id).first()
    if state:
        print("{}".format(state.id))
    else:
        print("Not found")
    session.close()