#!/usr/bin/python3
"""
 script that lists all State objects from the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    session = sessionmaker(bind=engine)()

    for idx in session.query(State.name, City.id, City.name).join(
            City, City.state_id == State.id).order_by(City.id):
        print("{}: ({}) {}".format(idx[0], idx[1], idx[2]))
    session.close()
