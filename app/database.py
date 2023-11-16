from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from psycopg2.extras import RealDictCursor
import time

# SQLALCHEMY_DATABASE_URL = "postgresql://<username>:<password>@<ip-address/hostname>:<database port>/<database_name>"

SQLALCHEMY_DATABASE_URL = f'postgresql://username:password@db:5432/postgres'

max_retries = 5
retry_interval = 5

def create_engine_with_retry(url, max_retries, retry_interval):
    retry_count = 0
    while True:
        try:
            engine = create_engine(url)
            engine.connect()
            return engine
        except Exception as e:
            retry_count += 1
            if retry_count > max_retries:
                raise
            print(f"Retrying in {retry_interval} seconds ({retry_count}/{max_retries})...")
            time.sleep(retry_interval)

engine = create_engine_with_retry(SQLALCHEMY_DATABASE_URL, max_retries, retry_interval)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
