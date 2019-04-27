import uuid

import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base  


POSTGRES_USER = 'postgres'
POSTGRES_PASSWORD = 'chungus'
POSTGRES_HOST = 'localhost'
POSTGRES_PORT = 5435
POSTGRES_DB = 'realestate'


db_string = 'postgres://{user}:{password}@{host}:{port}/{db}'.format(
  user=POSTGRES_USER,
  password=POSTGRES_PASSWORD,
  host=POSTGRES_HOST,
  port=POSTGRES_PORT,
  db=POSTGRES_DB
)

db = sa.create_engine(db_string)

base = declarative_base()

class RealestateApartment(base):   
    __tablename__ = POSTGRES_DB 

    fingerprint = sa.Column(sa.String, primary_key=True) 

    # Mandatory
    title = sa.Column(sa.String, nullable=False) 
    description = sa.Column(sa.String, nullable=False)
    posted_date = sa.Column(sa.DateTime, nullable=False)

    # Nullable
    partitioning = sa.Column(sa.String)
    surface = sa.Column(sa.Integer)
    building_year = sa.Column(sa.String)
    floor = sa.Column(sa.Integer)
    number_of_rooms = sa.Column(sa.Integer)
    terrace = sa.Column(sa.Boolean)
    parking = sa.Column(sa.Boolean)
    cellar = sa.Column(sa.Boolean)
    source_website = sa.Column(sa.String)
    source_offer = sa.Column(sa.String)
    neightbourhood = sa.Column(sa.String)


def get_postgres_session():
    # To fix db table changes errors enable once
    # db.execute('DROP TABLE realestate;')
    base.metadata.create_all(db)
    Session = sa.orm.sessionmaker(db)  
    return Session()