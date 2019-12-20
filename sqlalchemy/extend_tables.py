from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

AlchemyBase = declarative_base()

class User(AlchemyBase):

    __tablename__ = "user"

    id = Column(Integer,  primary_key=True)
    name = Column(String, nullable=False, unique=True)
    some_relation = relationship("BaseTable") # 1 User - n BaseTable

    def __init__(self,  name: str):
        self.name = name

    def __str__(self):
        return "User [id: {0}, name: {1}]".format(self.id, self.name)



class BaseTable(AlchemyBase):
    """
    Base class for Joined Table Inheritance
    inspired by: https://docs.sqlalchemy.org/en/13/orm/inheritance.html
    """

    __tablename__ = "base_table"

    id = Column(Integer, primary_key=True)
    type = Column(Integer)
    user_id = Column(Integer, ForeignKey("user.id"))

    def __init__(self, type: str):
        self.type = type

    __mapper_args__ = {
        "polymorphic_identity": "Base_Type",
        "polymorphic_on": type
    }


class ExtendedTable1(BaseTable):

    __tablename__ = "extended_table_1"

    id = Column(Integer, ForeignKey('base_table.id'), primary_key=True)
    something = Column(Integer)

    def __init__(self, something: int):
        super().__init__("Type_1")
        self.something = something

    __mapper_args__ = {
        "polymorphic_identity": "Type_1",
    }


class ExtendedTable2(BaseTable):

    __tablename__ = "extended_table_2"

    id = Column(Integer, ForeignKey('base_table.id'), primary_key=True)

    def __init__(self):
        super().__init__("Type_2")

    __mapper_args__ = {
        "polymorphic_identity": "Type_2",
    }

if __name__ == "__main__":

    engine = create_engine("sqlite:///data.db")
    AlchemyBase.metadata.drop_all(engine) # löschen aller Tabellen on Startup
    AlchemyBase.metadata.create_all(engine) # datenbank neu erstellen
    Session = sessionmaker(engine)
    session = Session()

    user = User("name")
    table1 = ExtendedTable1(42)
    table2 = ExtendedTable2()
    user.some_relation = [table1, table2]
    session.add(table1)
    session.add(table2)
    session.add(user)

    session.commit()