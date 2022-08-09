from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


SqlAlchemyBase = declarative_base()

class User(SqlAlchemyBase):

    __tablename__ = "user"

    id = Column(Integer,  primary_key=True)
    name = Column(String, nullable=False, unique=True)

    def __init__(self,  name: str):
        self.name = name

    def __repr__(self):
        return "User [id: {0}, name: {1}]".format(self.id, self.name)

if __name__ == "__main__":

    engine = create_engine("sqlite:///data.db")
    SqlAlchemyBase.metadata.create_all(engine)
    Session = sessionmaker(engine)
    session = Session()

    user = User("Batman")
    session.add(user)
    session.commit()

