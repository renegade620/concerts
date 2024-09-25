# imports
from models import Session, Band, Venue, Concert

# create new session
session = Session()

# example instances
band1 = Band(name="Le Band", hometown="Busia")
band2 = Band(name="Sauti Sol", hometown="Kakamega")
venue1 = Venue(title="Uhuru Park", city="Nairobi")
venue2 = Venue(title="Uhuru Gardens", city="Mombasa")
concert1 = Concert(date="1/1/2024", band=band1, venue=venue1)
concert2 = Concert(date="1/8/2024", band=band2, venue=venue2)
concert3 = Concert(date="1/12/2024", band=band1, venue=venue2)

session.add_all([band1, band2, venue1, venue2, concert1, concert2, concert3])
session.commit()

# bands info
all_bands = session.query(Band).all()
for band in all_bands:
    print(f"Band: {band.name} from {band.hometown}")
    
    # concerts for this band
    concerts = band.get_concerts()
    print(f"Concerts for {band.name}:")
    for concert in concerts:
        print(f"  - Date: {concert.date}, Venue: {concert.venue.title}")
    
    # venues this band has performed at
    venues = band.venues(session)
    print(f"Venues {band.name} has performed at:")
    for venue in venues:
        print(f"  - {venue.title} in {venue.city}")
    
    print()

# venues info
all_venues = session.query(Venue).all()
for venue in all_venues:
    print(f"Venue: {venue.title} in {venue.city}")
    
    # concerts for this venue
    concerts = venue.get_concerts()
    print(f"Concerts at {venue.title}:")
    for concert in concerts:
        print(f"  - Date: {concert.date}, Band: {concert.band.name}")
    
    # bands that have performed at this venue
    bands = venue.bands(session)
    print(f"Bands that have performed at {venue.title}:")
    for band in bands:
        print(f"  - {band.name}")
    
    print()

# close session
session.close()
