#!/usr/bin/python3

"""list state object from hbtn_0e_6_usa database where theyre is an a """


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    eng = create_engine(
        f'mysql+mysqldb://{mysql_username}:{mysql_password}@localhost:3305/'
        f'{database_name}'
        )
    Ses = sessionmaker(bind=eng)
    ses = Ses()
    states = ses.query(State).filter(State.name.like('%a%'))\
        .order_by(State.id).all()

    for state in states:
        print(f"{state.id}: {state.name}")

    ses.close()
