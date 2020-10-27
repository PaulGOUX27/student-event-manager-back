from api.core import Mixin
from .base import db
from sqlalchemy.orm import relationship
# from .associationTables import association_table_event_event_category

from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

association_table_event_event_category = Table('event_event_category', Base.metadata,
                                               Column('left_id', Integer, ForeignKey('left.id')),
                                               Column('right_id', Integer, ForeignKey('right.id'))
                                               )


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
