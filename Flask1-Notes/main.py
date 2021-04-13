from flask import Flask, render_template, request

app = Flask(__name__)

#1.define the route
#2.define a function to handel the route
@app.route("/")
def index():
  return render_template("index.html")

# try to create a greet route
@app.route("/greet")
def greet():
  # that shows the greet.html file
  return render_template("greet.html", name = request.args.get("name"))
# inside greet.html h2 that says Welcome, your name.

# ------- FOR THURSDAY -------
# create a new route called /movies
# that shows a favorite move the user types in
# change the index.html file to ask for a movie
# instead of a name.
# movies.html should say...
# Your favorite move is XXXXXXXXXX

# leave at the bottom of the file
# this strats the webserver on relpit
if __name__ == "__main__":
  app.run("0.0.0.0")
