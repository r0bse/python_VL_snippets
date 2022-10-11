from getpass import getpass

from passlib.hash import bcrypt
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)

    name = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)

    def __init__(self,  name: str,  password: str):
        self.name = name
        self.password = password


if __name__ == "__main__":
    engine = create_engine("sqlite:///save_password.db")
    Base.metadata.drop_all(engine)  # löschen aller Tabellen on Startup
    Base.metadata.create_all(engine)  # datenbank neu erstellen
    Session = sessionmaker(engine)
    session = Session()

    password = getpass()
    hasher = bcrypt.using(rounds=13)  # Make it slower
    hashed_password = hasher.hash(password)

    user = User("User", hashed_password)
    session.add(user)

    session.commit()