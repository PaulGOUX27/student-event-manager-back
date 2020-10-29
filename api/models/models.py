from api.core import Mixin
from .base import db
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

event_event_categories = db.Table('event_event_categories',
                                  db.Column('event_id', db.Integer, db.ForeignKey('event.id'), primary_key=True),
                                  db.Column('event_category_id', db.Integer, db.ForeignKey('event_category.id'),
                                            primary_key=True)
                                  )


class Event(Mixin, db.Model):

    id = db.Column(db.Integer, primary_key=True)
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    place = db.Column(db.String)
    description = db.Column(db.String)
    title = db.Column(db.String)
    event_categories = db.relationship(
        "EventCategory",
        secondary=event_event_categories, lazy='subquery',
        backref=db.backref('events', lazy=True))

    def __init__(self, start_date: datetime, end_date: datetime, place: str, description: str, title: str):
        self.place = place
        self.title = title
        self.description = description
        self.end_date = end_date
        self.start_date = start_date

    def __repr__(self):
        return f"<Event {self.title}>"


class EventCategory(Mixin, db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return f"<EventCategory {self.name}>"
