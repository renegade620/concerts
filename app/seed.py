# imports
from models import Session, Band, Venue, Concert

# create new session
session = Session()

# example instances
band1 = Band(name="Le Band", hometown="Busia")
band2 = Band(name="Sauti Sol", hometown="Kakamega")
band3 = Band(name="Elani", hometown="Nairobi")
venue1 = Venue(title="Uhuru Park", city="Nairobi")
venue2 = Venue(title="Uhuru Gardens", city="Mombasa")
venue3 = Venue(title="KICC", city="Nairobi")
concert1 = Concert(date="1/1/2024", band=band1, venue=venue1)
concert2 = Concert(date="1/8/2024", band=band2, venue=venue2)
concert3 = Concert(date="1/12/2024", band=band1, venue=venue2)
concert4 = Concert(date="1/15/2024", band=band3, venue=venue3)
concert5 = Concert(date="1/20/2024", band=band2, venue=venue3)
concert6 = Concert(date="1/25/2024", band=band1, venue=venue3)

session.add_all([band1, band2, venue1, venue2, venue3, concert1, concert2, concert3, concert4, concert5, concert6])
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

print("Concert Methods:")
print(f"Is concert1 a hometown show? {concert1.hometown_show()}")
print(f"Concert1 introduction: {concert1.introduction()}")
print()


# Band methods
print("Band Methods:")
# play_in_venue
band1.play_in_venue(session, venue3, "2/1/2024")
print(f"Added new concert for {band1.name} at {venue3.title}")

# all_introductions
print(f"{band1.name} introductions:")
for intro in band1.all_introductions():
    print(intro)

# most_performances
most_performing_band = Band.most_performances(session)
print(f"Band with most performances: {most_performing_band.name}")
print()

print("Venue Methods:")
# concert_on
date_to_check = "1/15/2024"
concert_on_date = venue3.concert_on(date_to_check)
if concert_on_date:
    print(f"Concert at {venue3.title} on {date_to_check}: {concert_on_date.band.name}")
else:
    print(f"No concert at {venue3.title} on {date_to_check}")

# most_frequent_band
most_frequent_band = venue3.most_frequent_band()
print(f"Most frequent band at {venue3.title}: {most_frequent_band.name}")

# close session
session.close()
