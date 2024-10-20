from flask import Flask, render_template
from .db import Config, Departure, Tour

app = Flask(__name__)


# ADD ROUTES
from . import routes
