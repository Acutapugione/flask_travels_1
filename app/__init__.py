from flask import Flask, render_template
from .db import Config, Departure, Tour

app = Flask(__name__)


# ADD ROUTES


@app.get("/")
def index():
    url = "https://http.cat/images/"
    items = [f"{url}{x}.jpg" for x in [101, 404, 500, 412]]
    return render_template("index.html", items=items)
