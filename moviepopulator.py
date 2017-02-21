from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from movie_database_setup import Movie, Base

engine = create_engine('sqlite:///movieinformation.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

# add movie information to SQLite database

toy_story = Movie(title="Toy Story",
                  storyline="A story of a boy and his toys that come to life",
                  poster_image_url="goo.gl/S0lMXL",
                  trailer_youtube_url="goo.gl/pqDLZF")
session.add(toy_story)
session.commit()

avatar = Movie(title="Avatar", storyline="A marine on an alien planet",
               poster_image_url="goo.gl/WgQRSm",
               trailer_youtube_url="goo.gl/pdpAuD")
session.add(avatar)
session.commit()

yourname = Movie(title="Your Name", storyline="Two strangers find themselves "
                                              "linked in a bizarre way.",
                 poster_image_url="goo.gl/0U66Zw",
                 trailer_youtube_url="goo.gl/vPbkGw")
session.add(yourname)
session.commit()

dead_poets_society = Movie(title="Dead Poets Society",
                           storyline="English teacher John Keating inspires "
                                     "his students to look at poetry "
                                     "with a different perspective of "
                                     "authentic knowledge and feelings.",
                           poster_image_url="goo.gl/UgWDgp",
                           trailer_youtube_url="https://goo.gl/85aMvU")
session.add(dead_poets_society)
session.commit()

three_idiots = Movie(title="3 idiots",
                     storyline="Two friends are searching "
                               "for their long lost companion. "
                               "They revisit their college days.",
                     poster_image_url="https://goo.gl/hgDCuC",
                     trailer_youtube_url="https://goo.gl/Syd3bI")

session.add(three_idiots)
session.commit()

the_shawshank_redemption = Movie(title="The Shawshank Redemption",
                                 storyline="Two imprisoned men bond "
                                           "over a number of years, "
                                           "finding solace and eventual "
                                           "redemption through acts of "
                                           "common decency.",
                                 poster_image_url="https://goo.gl/pKmq6z",
                                 trailer_youtube_url="https://goo.gl/PhC131")
session.add(the_shawshank_redemption)
session.commit()

# to check if adding is done.
print "added movies!"
