from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
import psycopg2

engine = create_engine('postgresql://postgres:04041954-@localhost/API_interview')
session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
Base.query = session.query_property()


def create_db():
    Base.metadata.create_all(engine)