from api.core import Mixin
from .base import db
from datetime import datetime
from sqlalchemy.orm import relationship
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

association_table_event_event_category = Table('event_event_category', Base.metadata,
                                               Column('left_id', Integer, ForeignKey('left.id')),
                                               Column('right_id', Integer, ForeignKey('right.id'))
                                               )


class Event(Mixin, db.Model):
    """Event Table."""

    id = db.Column(db.Integer, primary_key=True)
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    place = db.Column(db.String)
    description = db.Column(db.String)
    title = db.Column(db.String)
    event_categories = relationship(
        "EventCategory",
        secondary=association_table_event_event_category,
        back_populates="events")

    def __init__(self, start_date: datetime, end_date: datetime, place: str, description: str, title: str):
        self.place = place
        self.title = title
        self.description = description
        self.end_date = end_date
        self.start_date = start_date

    def __repr__(self):
        return f"<Event {self.title}>"


class EventCategory(Mixin, db.Model):
    """Event Category Table."""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    events = relationship(
        "Event",
        secondary=association_table_event_event_category,
        back_populates="event_categories")

    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return f"<EventCategory {self.name}>"