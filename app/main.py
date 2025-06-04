# /home/ubuntu/currency-ingestion_refactored/currency-ingestion/app/main.py

import os
from dotenv import load_dotenv, find_dotenv

# Import functions from other modules
from app.api_client import fetch_latest_rates
from app.data_handler import transform_data
from app.storage_handler import setup_database, save_currency_data, Currency # Import Currency model too

def run_etl_pipeline():
    """Runs the simplified ETL pipeline.
    
    Returns:
        True if the pipeline ran successfully, False otherwise.
    """
    print("Starting simplified ETL run...")

    # --- Configuration --- 
    print("Loading environment variables...")
    dotenv_path = find_dotenv()
    if not dotenv_path:
        print("Error: .env file not found. Please ensure it exists in the project root.")
        return False
    load_dotenv(dotenv_path=dotenv_path, override=True) # Use override based on previous debug
    print(f"Loaded environment variables from: {dotenv_path}")

    api_key = os.getenv("CURRENCY_API_KEY")
    db_url = os.getenv("DATABASE_KEY") # Ensure this matches your .env file

    if not api_key:
        print("Error: CURRENCY_API_KEY not found in environment variables.")
        return False
    if not db_url:
        print("Error: DATABASE_KEY not found in environment variables.")
        return False
    print("API Key and Database URL loaded.")

    # --- Database Setup --- 
    print("Setting up database connection and tables...")
    engine, SessionLocal = setup_database(db_url)
    if not engine or not SessionLocal:
        print("ETL run failed: Could not set up database.")
        return False
    print("Database setup complete.")

    # --- ETL Steps --- 
    # 1. Extract
    print("--- Step 1: Extracting data ---")
    raw_data = fetch_latest_rates(api_key)
    if not raw_data:
        print("ETL run failed: Could not extract data from API.")
        return False

    # 2. Transform
    print("--- Step 2: Transforming data ---")
    currency_object = transform_data(raw_data)
    if not currency_object:
        print("ETL run failed: Could not transform data.")
        return False

    # 3. Load
    print("--- Step 3: Loading data ---")
    session = SessionLocal() # Create a new session for this transaction
    success = False
    try:
        success = save_currency_data(session, currency_object)
        if not success:
             print("ETL run failed: Could not save data to database.")
             # No need to return here, finally block will still execute
    finally:
        session.close() # Ensure session is always closed
        print("Database session closed.")
        
    if not success:
        return False # Return failure if saving failed

    print("\nSimplified ETL run completed successfully.")
    return True

# --- Main execution block --- 
if __name__ == "__main__":
    print("Script started as main program (simplified functional version).")
    pipeline_success = run_etl_pipeline()
    if not pipeline_success:
        print("Pipeline execution finished with errors.")
        exit(1) # Exit with a non-zero code to indicate failure
    else:
        print("Pipeline execution finished successfully.")

