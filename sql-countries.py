from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()

# create a class-based model for the "Programmer" table
class Country(base):
    __tablename__ = "Country"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    capital = Column(String)

# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)

# creating records on our Progammer table
spain = Country(
    name = "Spain",
    capital = "Madrid"
)

# add each instance of our programmers to our session
session.add(spain)

# commit our session to the database
session.commit()

# query the database to find all Counrties
countries = session.query(Country)
for country in countries:
    print(
        country.id,
        country.name,
        country.capital,
        sep=" | "
    )