import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Movie(Base):
    __tablename__ = 'movie'

    id = Column(Integer, primary_key=True)
    title = Column(String(80), nullable = False)
    storyline = Column(String(300))
    poster_image_url = Column(String(300))
    trailer_youtube_url = Column(String(300))

engine = create_engine('sqlite:///movieinformation.db')
Base.metadata.create_all(engine)
