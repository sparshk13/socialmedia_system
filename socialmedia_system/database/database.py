import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

load_dotenv()

user = os.getenv("USER_NAME")
password = os.getenv("PASSWORD")
db_name = os.getenv("DB_NAME")

DATABSE_URL = f"postgresql+psycopg2://{user}:{password}@localhost:5432/{db_name}"

engine = create_engine(DATABSE_URL, echo=True)

# session = sessionmaker(engine)
Session = sessionmaker(autoflush=False, bind=engine)


Base = declarative_base()


def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()