from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base  # Adjust this import based on your models module

# Database configuration
DATABASE_URL = "sqlite:///database.db"  # Use your desired database URL

# Create the database engine
engine = create_engine(DATABASE_URL)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Create all tables
Base.metadata.create_all(bind=engine)
