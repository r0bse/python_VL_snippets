from abc import abstractmethod

from sqlalchemy import create_engine, Column, Integer, Float, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()


class Club(Base):
    __tablename__ = "club"

    id = Column(Integer, primary_key=True)

    club_name = Column(String(255), nullable=False, unique=True)
    players = relationship("Player", back_populates="club")

    def __init__(self,  name: str):
        self.club_name = name


class Player(Base):
    __tablename__ = "player"

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    discriminator_column = Column(String(50))

    # create a Foreign key table which references a concrete Key Column at the related table
    club_id = Column(ForeignKey('club.id'))
    # create a relationship to related table which back populates to the named attribute
    club = relationship("Club", back_populates="players")

    def __init__(self,  name: str):
        self.name = name

    __mapper_args__ = {
        'polymorphic_identity': "player",
        'polymorphic_on': discriminator_column
    }


class Footballer(Player):
    number = Column(Integer())

    def __init__(self, name: str, number: int):
        self.number = number
        super().__init__(name)

    __mapper_args__ = {
        'polymorphic_identity': "footballer"
    }


class ProfessionalFootballer(Footballer):
    salary = Column(Integer())

    def __init__(self, name: str, number: int, salary: int):
        self.salary = salary
        super().__init__(name, number)

    __mapper_args__ = {
        'polymorphic_identity': "professional_footballer"
    }


class Bowler(Player):
    bowling_average = Column(Float())

    def __init__(self, name: str, average: float):
        self.bowling_average = average
        super().__init__(name)

    __mapper_args__ = {
        'polymorphic_identity': "bowler"
    }


if __name__ == "__main__":
    engine = create_engine("sqlite:///single_table_strategy.db")
    Base.metadata.drop_all(engine)  # löschen aller Tabellen on Startup
    Base.metadata.create_all(engine)  # datenbank neu erstellen
    Session = sessionmaker(engine)
    session = Session()

    footballer = Footballer("Footballer", 96)
    bowler = Bowler("Bowler", 8.9)
    professional = ProfessionalFootballer("Professional Footballer", 10, 100000)

    hertha = Club("Hertha BSC")
    union = Club("1.FC Union")

    hertha.players = [bowler, footballer]
    union.players = [professional]
    session.add(hertha)
    session.add(union)
    # session.add_all([bowler, footballer, professional])

    session.commit()


