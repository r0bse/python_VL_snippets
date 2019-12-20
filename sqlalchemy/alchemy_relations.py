from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

SqlAlchemyBase = declarative_base()

class User(SqlAlchemyBase):

    __tablename__ = "user"

    id = Column(Integer, primary_key = True)
    name = Column(String, nullable=False)

    emails = relationship("Email")

    def __init__(self, name = ""):
        self.name = name

class Email(SqlAlchemyBase):

    __tablename__ = "email"

    id = Column(Integer, primary_key = True)
    email_address = Column(String, nullable=False)

    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates = "emails")

    def __init__(self, email = "", user = None):
        """"
        a constructor can set relations on its own, when params are given
        """
        self.email_address = email
        if user != None:
            self.user_id = user.id



def manage_relations_manually():
    user = User()
    user.name = "Klaus Peter"
    email = Email()
    email.email_address = "klaus@peter.de"
    session.add(user)
    session.add(email)
    # session.commit() # relation wurde nicht gesetzt

    user.emails = [email] # relationship erwartet eine Liste
    session.commit() # relation wurde gesetzt


def manage_relations_automatically():
    user = User("Klaus Peter der 2.")
    session.add(user)
    session.commit()
    email = Email("klaus@peter.com", user) # user muss vorher gespeichert werden, da sonst die (autogenerierte ID) nicht gesetzt ist
    session.add(email)
    session.commit()

if __name__ == "__main__":

    engine = create_engine("sqlite:///data.db")
    SqlAlchemyBase.metadata.drop_all(engine) # löschen aller Tabellen on Startup
    SqlAlchemyBase.metadata.create_all(engine) # datenbank neu erstellen
    Session = sessionmaker(engine)
    session = Session()

    manage_relations_automatically()
    manage_relations_manually()