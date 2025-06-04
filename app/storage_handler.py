# /home/ubuntu/currency-ingestion_refactored/currency-ingestion/app/storage_handler.py

from sqlalchemy import create_engine, Column, String, Float, Integer, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime

# Define the base for declarative class definitions
Base = declarative_base()

# Define the data model
class Currency(Base):
    """Data model for storing currency exchange rates."""
    __tablename__ = "currency" # Table name in the database

    id = Column(Integer, primary_key=True) # Auto-incrementing primary key
    Real = Column(Float) # BRL value
    Euro = Column(Float) # EUR value
    timestamp = Column(DateTime, default=datetime.now()) # Timestamp of data retrieval (UTC)

def setup_database(db_url: str):
    """Sets up the database engine and session maker.

    Args:
        db_url: The database connection URL.

    Returns:
        A tuple containing the engine and the Session class, or (None, None) on error.
    """
    if not db_url:
        print("Error: Database URL cannot be empty.")
        return None, None
    try:
        engine = create_engine(db_url)
        SessionLocal = sessionmaker(bind=engine)
        print("Database engine and session maker created successfully.")
        # Create tables if they don't exist
        print(f"Attempting to create tables for metadata: {Base.metadata.tables.keys()}")
        Base.metadata.create_all(bind=engine)
        print("Tables checked/created successfully.")
        return engine, SessionLocal
    except SQLAlchemyError as e:
        print(f"Error setting up database: {e}")
        return None, None

def save_currency_data(session, currency_data: Currency):
    """Saves a Currency data object to the database using the provided session.
    
    Args:
        session: An active SQLAlchemy session.
        currency_data: The Currency object to save.
    """
    if not session or not currency_data:
        print("Error: Invalid session or data provided for saving.")
        return False
        
    try:
        session.add(currency_data)
        session.commit()
        print(f"Successfully saved data to PostgreSQL: Real={currency_data.Real}, Euro={currency_data.Euro}")
        return True
    except SQLAlchemyError as e:
        print(f"Error saving data to database: {e}")
        session.rollback() # Roll back the transaction on error
        return False

