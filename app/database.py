from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from psycopg2.extras import RealDictCursor
import time

# SQLALCHEMY_DATABASE_URL = "postgresql://<username>:<password>@<ip-address/hostname>:<database port>/<database_name>"

# Use this for Docker Compose
# SQLALCHEMY_DATABASE_URL = f'postgresql://root:root@db:5432/test_db'

# Use this for Kubernetes Deployment
SQLALCHEMY_DATABASE_URL = 'postgresql://your_database_user:your_database_password@postgres-service:5432/your_database_name'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
 
Base = declarative_base() 

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
