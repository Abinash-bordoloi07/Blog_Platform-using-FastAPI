from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = 'sqlite:///./blog.db'
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"


# connect_args needed only for sqlite and not for postgresql and other databases
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})



SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()  