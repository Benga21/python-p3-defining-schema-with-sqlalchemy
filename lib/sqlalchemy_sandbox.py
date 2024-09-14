#!/usr/bin/env python3

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'  # Table name in the database

    id = Column(Integer(), primary_key=True)  # Primary key column
    name = Column(String())  # Column for student names

# If script is run directly, persist the schema
if __name__ == '__main__':

    engine = create_engine('sqlite:///students.db')
    Base.metadata.create_all(engine)
    print("Schema persisted successfully!")