from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from movie_database_setup import Movie, Base

engine = create_engine('sqlite:///movieinformation.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

toy_story = Movie(title="Toy Story", storyline="A story of a boy and his toys that come to life",
                  poster_image_url="https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                  trailer_youtube_url ="https://www.youtube.com/watch?v=KYz2wyBy3kc")
session.add(toy_story)
session.commit()

avator = Movie(title="Avator", storyline="A marine on an alien planet",
                poster_image_url="https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                trailer_youtube_url="https://www.youtube.com/watch?v=5PSNL1qE6VY")
session.add(avator)
session.commit()

yourname = Movie(title="Your Name",storyline="Two strangers find themselves linked in a bizarre way.",
                poster_image_url="https://upload.wikimedia.org/wikipedia/en/0/0b/Your_Name_poster.png",
                trailer_youtube_url="https://www.youtube.com/watch?v=s0wTdCQoc2k")
session.add(yourname)
session.commit()

dead_poets_society = Movie(title="Dead Poets Society",
                     storyline="English teacher John Keating inspires his students to look at poetry with a different perspective of authentic knowledge and feelings.",
                     poster_image_url="https://upload.wikimedia.org/wikipedia/en/4/49/Dead_poets_society.jpg",
                      trailer_youtube_url="https://www.youtube.com/watch?v=4lj185DaZ_o")
session.add(dead_poets_society)
session.commit()

three_idiots = Movie(title="3 idiots",
                     storyline="Two friends are searching for their long lost companion. They revisit their college days.",
                     poster_image_url="https://upload.wikimedia.org/wikipedia/en/d/df/3_idiots_poster.jpg",
                      trailer_youtube_url="https://www.youtube.com/watch?v=K0eDlFX9GMc")

session.add(three_idiots)
session.commit()

the_shawshank_redemption = Movie(title="The Shawshank Redemption",
                     storyline="Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.",
                     poster_image_url="https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",
                     trailer_youtube_url= "https://www.youtube.com/watch?v=6hB3S9bIaco")
session.add(the_shawshank_redemption)
session.commit()

print "added movies!"
