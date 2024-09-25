# Phase 3 Code Challenge: Concerts

## Project Overview

a **Concerts** domain and a system to manage bands, venues, and concerts. A **Band** can play multiple concerts, and a **Venue** can host multiple concerts, forming a many-to-many relationship between the two. Each **Concert** belongs to one **Band** and one **Venue**.

## Domain Models

### 1. Band
- **Attributes**: `name`, `hometown`
- **Relationships**: A band can play many concerts.

### 2. Venue
- **Attributes**: `title`, `city`
- **Relationships**: A venue can host many concerts.

### 3. Concert
- **Attributes**: `date`, `band_id`, `venue_id`
- **Relationships**: A concert belongs to a band and a venue.

### Schema
- **Bands Table**
  - `name`: String
  - `hometown`: String

- **Venues Table**
  - `title`: String
  - `city`: String

- **Concerts Table**
  - `date`: String
  - `band_id`: ForeignKey to `Band`
  - `venue_id`: ForeignKey to `Venue`

## Project Setup

### Prerequisites

- **SQLAlchemy**: You'll need SQLAlchemy installed to manage the database models.
  
  Install it via pip:
  ```bash
  pip install SQLAlchemy
  ```

- **SQLite**: This project uses an SQLite database for simplicity.

### Migrations

You will need to create migrations for the tables (bands, venues, and concerts). Migrate the **bands** and **venues** tables first, then add a migration for the **concerts** table. The concerts table should include:
- `date`: Stores the concert date as a string.
- `band_id`: Foreign key to `Band`.
- `venue_id`: Foreign key to `Venue`.

### Running the Project

1. Create the database and apply the migrations to set up the schema.
2. Create instances of `Band`, `Venue`, and `Concert` to populate the database.
3. Use the methods described in the "Deliverables" section below to interact with the models and test the functionality.

## Deliverables

### Object Relationship Methods

#### Concert
- `Concert.get_band()`: Returns the `Band` instance for the concert.
- `Concert.get_venue()`: Returns the `Venue` instance for the concert.

#### Venue
- `Venue.get_concerts()`: Returns all concerts at the venue.
- `Venue.get_bands()`: Returns all bands who performed at the venue.

#### Band
- `Band.get_concerts()`: Returns all concerts the band has played.
- `Band.get_venues()`: Returns all venues where the band has performed.

### Aggregate and Relationship Methods

#### Concert
- `Concert.hometown_show()`: Returns `True` if the concert is in the band's hometown, `False` otherwise.
- `Concert.introduction()`: Returns a string introducing the band at the concert, formatted as:
  ```
  "Hello {venue city}!!!!! We are {band name} and we're from {band hometown}"
  ```

#### Band
- `Band.play_in_venue(venue, date)`: Creates a new concert for the band at the given venue and date.
- `Band.all_introductions()`: Returns a list of strings representing all introductions for the band, with each introduction formatted as:
  ```
  "Hello {venue city}!!!!! We are {band name} and we're from {band hometown}"
  ```
- `Band.most_performances()`: Class method that returns the band with the most concerts.

#### Venue
- `Venue.concert_on(date)`: Returns the first concert at the venue on the specified date.
- `Venue.most_frequent_band()`: Returns the band with the most concerts at the venue.

## Conclusion

This project demonstrates how to manage a many-to-many relationship between bands and venues through concerts. By creating instance and class methods in the models, you can easily query and manipulate data, including more complex queries like finding the band with the most performances or introducing a band at a concert.

Powered by franklinegift@gmail.com