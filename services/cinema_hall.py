from db.models import CinemaHall
from django.db.models import QuerySet


def get_cinema_halls() -> QuerySet:
    cinema_halls = CinemaHall.objects.all()
    return cinema_halls


def create_cinema_hall(
        hall_name: str,
        hall_rows: str,
        hall_seats_in_row: str,
) -> CinemaHall:
    cinema_hall = CinemaHall.objects.create(
        name=hall_name,
        rows=hall_rows,
        seats_in_row=hall_seats_in_row,
    )
    return cinema_hall
