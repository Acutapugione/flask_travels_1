# from __future__ import annotations
# from typing import List

from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy.orm import Mapped
from .helpers import AutoincrementID


class Departure(AutoincrementID, table=True):
    name: str
    desc: str
    tours: list["Tour"] = Relationship(back_populates="departure")

    @staticmethod
    def mock_data() -> list["Departure"]:
        return [
            Departure(name=f"Напрям №{x}", desc="Тестовий набір даних")
            for x in range(5)
        ]
