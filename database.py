from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql://yash:1234@localhost:5432/devtracker")
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()