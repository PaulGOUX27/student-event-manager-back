# this file structure follows http://flask.pocoo.org/docs/1.0/patterns/appfactories/
# initializing db in api.models.base instead of in api.__init__.py
# to prevent circular dependencies
from .base import db
from .EventCategory import EventCategory
from .associationTables import association_table_event_event_category
from .Event import Event

__all__ = ["Event", "EventCategory", "db", "association_table_event_event_category"]

# You must import all of the new Models you create to this page
