# movies_trailer_website

Server-side code to store a list of my favorite movies, including box art imagery and a movie trailer URL. You will then serve this data as a web page allowing visitors to review their movies and watch the trailers.

This project is written in python with sqlite as a database to store movies information like titles, story line, image url and youtube trailer. It uses Flask as framework.

To run the project
1. Insert movie data into SQLite database
```sh
$ python moviepopulator.py
```

2. Run python file to get created HTML file.
```sh
$ python entertainment_center.py
```
3. Open browser and go to either of the below urls
- http://localhost:8080/
- http://localhost:8080/movies
- http://localhost:8080/movies.html
