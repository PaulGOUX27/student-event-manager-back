from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

association_table_event_event_category = Table('event_event_category', Base.metadata,
                                               Column('left_id', Integer, ForeignKey('left.id')),
                                               Column('right_id', Integer, ForeignKey('right.id'))
                                               )
