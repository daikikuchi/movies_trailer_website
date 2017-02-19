import fresh_tomatoes
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from movie_database_setup import Movie, Base
from flask import Flask, render_template
app = Flask(__name__)

# import Flask to create Web server.

engine = create_engine('sqlite:///movieinformation.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
@app.route('/movies')
@app.route('/movies.html')
def movie_list():
    all_rows = session.query(Movie).all()
    # to create HTML file from all the movies from database
    fresh_tomatoes.create_movies_page(all_rows)
    return render_template("movies.html")


# set up localhost.
if __name__ == '__main__':
    app.debug = True
    app.run(host = 'localhost', port = 8080)
