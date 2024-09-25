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

    # Object Relationship Methods
    def get_concerts(self):
        """return a collection of all the concerts that the Band has played"""
        return self.concerts

    def venues(self, session):
        """return a collection of all the venues the band has performed at"""
        return (
            session.query(Venue)
            .join(Concert)
            .filter(Concert.band == self)
            .distinct()
            .all()
        )

    # Aggregate and Relationship Methods
    def play_in_venue(self, session, venue, date):
        """takes a venue (Venue instance) and date (as a string) as arguments creates a new concert for the band in that venue on that date"""
        new_concert = Concert(band=self, venue=venue, date=date)
        session.add(new_concert)
        session.commit()

    def all_introductions(self):
        """returns an array of strings representing all the introductions for this band"""
        return [concert.introduction() for concert in self.concerts]

    @classmethod
    def most_performances(cls, session):
        """returns the Band instance for the band that has played the most concerts"""
        bands = session.query(cls).all()
        return max(bands, key=lambda band: len(band.concerts))


class Venue(Base):
    __tablename__ = "venues"

    id = Column(Integer(), primary_key=True)
    title = Column(String())
    city = Column(String())

    concerts = relationship("Concert", backref="venue")

    # Object Relationship Methods
    def get_concerts(self):
        """return a collection of concerts for that venue"""
        return self.concerts

    def bands(self, session):
        """returns a collection of all the bands who performed at the Venue"""
        return (
            session.query(Band)
            .join(Concert)
            .filter(Concert.venue == self)
            .distinct()
            .all()
        )

    # Aggregate and Relationship Methods
    def concert_on(self, date):
        return next((concert for concert in self.concerts if concert.date == date), None)
    
    def most_frequent_band(self):
        band_concert_count = {}
        for concert in self.concerts:
            band_concert_count[concert.band] = band_concert_count.get(concert.band, 0) + 1
        return max(band_concert_count, key=band_concert_count.get)


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
    def hometown_show(self):
        """returns true if the concert is in the band's hometown, false if it is not"""
        return self.venue.city == self.band.hometown

    def introduction(self):
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"


Base.metadata.create_all(engine)
