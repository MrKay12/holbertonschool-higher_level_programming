#!/usr/bin/python3

"""print Cities in hbtn_0e_14_usa database."""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
import sys

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    eng = create_engine(
        f'mysql+mysqldb://{mysql_username}:{mysql_password}@localhost:3306/'
        f'{database_name}'
        )
    Ses = sessionmaker(bind=eng)
    ses = Ses()

    cities = (
        ses.query(City, State)
        .filter(City.state_id == State.id)
        .order_by(City.id)
        .all()
        )

    for city, state in cities:
        print(f"{state.name}: ({city.id}) {city.name}")

    ses.close()
