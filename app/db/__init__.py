from sqlmodel import SQLModel, create_engine, Session


from .models import Departure, Tour


class Config:
    engine = create_engine("sqlite:///my_database.sql")
    session = Session(bind=engine)

    @classmethod
    def mock_up(cls):
        SQLModel.metadata.drop_all(cls.engine)

        SQLModel.metadata.create_all(cls.engine)
        tours = Tour.mock_data(Departure.mock_data())
        cls.session.add_all(tours)
        cls.session.commit()
