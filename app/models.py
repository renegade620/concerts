from sqlalchemy import Column, Integer, String, ForeignKey, Date, create_engine
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine("sqlite:///concerts.db")
Session = sessionmaker(bind=engine)

class Band(Base):
    __tablename__ = "bands"

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    hometown = Column(String())

    concerts = relationship("Concert", backref="band")

class Venue(Base):
    __tablename__ = "venues"

    id = Column(Integer(), primary_key=True)
    title = Column(String())
    city = Column(String())

    concerts = relationship("Concert", backref="venue")

class Concert(Base):
    __tablename__ = "concerts"

    id = Column(Integer(), primary_key=True)
    date = Column(Date())
    band_id = Column(Integer(), ForeignKey("bands.id"))
    venue_id = Column(Integer(), ForeignKey("venues.id"))

Base.metadata.create_all(engine)