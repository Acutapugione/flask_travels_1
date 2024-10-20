from .. import app
from ..db import (
    Departure,
    Tour,
    Config,
)
from sqlmodel import select
from flask import render_template


def get_departure_list() -> list["Departure"]:
    return list(Config.session.scalars(select(Departure)).all())


def get_tour_list(departure: Departure | int | None = None) -> list["Tour"]:
    lst = []
    if departure:
        if isinstance(departure, Departure):
            lst = Config.session.scalars(
                select(Tour).where(Tour.departure == departure)
            ).all()
        elif isinstance(departure, int):
            lst = Config.session.scalars(
                select(Tour).where(Tour.departure_id == departure)
            ).all()
    else:
        lst = Config.session.scalars(select(Tour)).all()
    return list(lst)


@app.get("/")
def index():
    return render_template(
        "index.html",
        items=get_departure_list() + get_tour_list(None),
        departures=get_departure_list(),
    )


from . import departure
