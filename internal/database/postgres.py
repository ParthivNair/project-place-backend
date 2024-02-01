from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

password = os.getenv("DB_PASS", "pass")

URL_DATABASE = f"postgresql://postgres:{password}@localhost:5432/postgres"

engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# def get_item():
#     # make query to database here with client
#     _ = postgres_client
#     results = "db results"
#     return results
