from flask import Flask, render_template, request

app = Flask(__name__)

# 1. define a route
# 2. define a function to handle the route
@app.route("/", methods=["GET", "POST"])
def index():
  if request.method == "POST":
    movie = request.form.get("movie", "ET")
    return render_template("movies.html", movie_title = movie)
  return render_template("index.html")

# create a /greet route
@app.route("/greet", methods=["GET", "POST"])
# that shows the greet.html file
def greet():
  return render_template("greet.html", name=request.form.get("name"))

# for next time....
# create a new route called movies
# that shows the movies.html file
# from the default route change index.html 
# to ask for a movie, when they hit submit
# go to and dispaly the movie route.
# Your favorite move is XXXXXXXXXXX
'''@app.route("/movies", methods=["GET", "POST"])
def movie():
  movie = request.form.get("movie", "Endgame")
  return render_template("movies.html",movie_title = movie)'''

# leave this at the bottom of your main.py file
if __name__ == "__main__":
  app.run("0.0.0.0")