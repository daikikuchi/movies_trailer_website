import fresh_tomatoes
import media
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from movie_database_setup import Movie, Base
from flask import Flask, request,redirect, render_template
app = Flask(__name__)

engine = create_engine('sqlite:///movieinformation.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
@app.route('/movies')
@app.route('/movies.html')
def movie_list():
    all_rows = session.query(Movie).all()
    movies=[]
    for r in all_rows:
         movie=media.Movie(r.title, r.storyline, r.poster_image_url, r.trailer_youtube_url)
         movies.append(movie)
    fresh_tomatoes.open_movies_page(movies)
    return render_template("movies.html")


if __name__ == '__main__':
    app.debug = True
    app.run(host = 'localhost', port = 8080)
