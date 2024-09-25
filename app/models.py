from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
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

    def get_concerts(self):
        """return a collection of all the concerts that the Band has played"""
        return self.concerts
    
    def venues(self, session):
        """return a collection of all the venues the band has performed at"""
        return session.query(Venue).join(Concert).filter(Concert.band == self).distinct().all()

class Venue(Base):
    __tablename__ = "venues"

    id = Column(Integer(), primary_key=True)
    title = Column(String())
    city = Column(String())

    concerts = relationship("Concert", backref="venue")

    def get_concerts(self): 
        """return a collection of concerts for that venue"""
        return self.concerts
    
    def bands(self, session):
        """returns a collection of all the bands who performed at the Venue"""
        return session.query(Band).join(Concert).filter(Concert.venue == self).distinct().all()


class Concert(Base):
    __tablename__ = "concerts"

    id = Column(Integer(), primary_key=True)
    date = Column(String())
    band_id = Column(Integer(), ForeignKey("bands.id"))
    venue_id = Column(Integer(), ForeignKey("venues.id"))

    # Object Relationship Methods
    def band(self):
        """returns Band instance for this concert"""
        return self.band
    
    def venue(self):
        """returns Venue instance for this concert"""
        return self.venue

    # Aggregate and Relationship Methods

Base.metadata.create_all(engine)