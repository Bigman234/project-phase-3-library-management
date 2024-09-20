from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

# Database URL
DATABASE_URL = "sqlite:///database.db"

# Create engine
engine = create_engine(DATABASE_URL)

# Base class for declarative models
Base = declarative_base()