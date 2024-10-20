# from __future__ import annotations
# from typing import List
import time
import random
from sqlmodel import SQLModel, Field, Relationship
from .helpers import AutoincrementID
from .departure import Departure
from decimal import Decimal


class Tour(AutoincrementID, table=True):
    name: str
    desc: str
    departure: Departure = Relationship(back_populates="tours")
    departure_id: int = Field(foreign_key=f"{Departure.__tablename__}.id")
    price: Decimal

    @staticmethod
    def mock_data(departures: list[Departure]) -> list["Tour"]:

        random.seed(time.time())
        return [
            Tour(
                name=f"Тур №{tour}({departure.name})",
                desc="Тестовий набір даних",
                departure=departure,
                price=Decimal(f"{random.random()*100}").quantize(Decimal("1.00")),
            )
            for tour in range(5)
            for departure in departures
        ]
