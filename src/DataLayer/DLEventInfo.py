from sqlobject import *
from src import conn


def process_event_into_db(event_details):
    _connection = conn