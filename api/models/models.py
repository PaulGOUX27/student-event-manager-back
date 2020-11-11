from .base import db
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_serializer import SerializerMixin

Base = declarative_base()

event_event_categories = db.Table('event_event_categories',
                                  db.Column('event_id', db.Integer, db.ForeignKey('event.id'), primary_key=True),
                                  db.Column('event_category_id', db.Integer, db.ForeignKey('event_category.id'),
                                            primary_key=True)
                                  )


class Event(db.Model, SerializerMixin):
    serialize_rules = ('-event_categories.events', '-person.events', '-person_id',)
    datetime_format = '%Y-%m-%dT%H:%M'

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
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'), nullable=False)

    def __init__(self, start_date: datetime, end_date: datetime, place: str, description: str, title: str, person_id=1,
                 event_categories=None):
        if event_categories is None:
            event_categories = []
        self.place = place
        self.title = title
        self.description = description
        self.end_date = end_date
        self.start_date = start_date
        self.person_id = person_id
        self.event_categories = event_categories

    def __repr__(self):
        return f"<Event {self.title}>"


class EventCategory(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return f"<EventCategory {self.name}>"


class Person(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String)
    password = db.Column(db.String)
    validate = db.Column(db.Boolean)
    firstname = db.Column(db.String)
    lastname = db.Column(db.String)
    events = db.relationship(
        "Event", backref='person', lazy=True)

    def __init__(self, login: str, password: str, validate: bool, firstname: str, lastname: str):
        self.login = login
        self.password = password
        self.validate = validate
        self.firstname = firstname
        self.lastname = lastname

    def __repr__(self):
        return f"<Person {self.login}>"
