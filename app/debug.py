from models import Session, Band, Venue, Concert

session = Session()

# Create band and venue instances
band1 = Band(name="Le Band", hometown="Busia")
band2 = Band(name="Sauti Sol", hometown="Kakamega")
venue1 = Venue(title="Uhuru Park", city="Nairobi")
venue2 = Venue(title="Uhuru Gardens", city="Mombasa")

# Create concert instances
concert1 = Concert(date="1/1/2024", band=band1, venue=venue1)
concert2 = Concert(date="1/8/2024", band=band2, venue=venue2)
concert3 = Concert(date="1/12/2024", band=band1, venue=venue2)

# Add a breakpoint
import ipdb; ipdb.set_trace()  # This should now work correctly

# Add all instances to the session
session.add_all([band1, band2, venue1, venue2, concert1, concert2, concert3])

# Commit the changes to the database
session.commit()
