from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

# Use sqlalchemy to import necessary modules to create SQLight database.

Base = declarative_base()


# Create class Movie with attributes
class Movie(Base):
    __tablename__ = 'movie'

    id = Column(Integer, primary_key=True)
    title = Column(String(80), nullable=False)
    storyline = Column(String(300))
    poster_image_url = Column(String(300))
    trailer_youtube_url = Column(String(300))


engine = create_engine('sqlite:///movieinformation.db')
Base.metadata.create_all(engine)
