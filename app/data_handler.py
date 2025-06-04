# /home/ubuntu/currency-ingestion_refactored/currency-ingestion/app/data_handler.py

from datetime import datetime
# Import the Currency model from storage_handler
# Assuming storage_handler will define the Currency model
from app.storage_handler import Currency 

def transform_data(api_data: dict) -> Currency | None:
    """Transforms raw API data (dictionary) into a Currency object.

    Args:
        api_data: The dictionary containing the data fetched from the API.
                  Expected format: {"data": {"BRL": value, "EUR": value, ...}}

    Returns:
        A Currency object populated with the extracted data and timestamp,
        or None if the required data ("BRL" or "EUR") is missing or invalid.
    """
    if not api_data or "data" not in api_data:
        print("Error: Invalid or empty API data received for transformation.")
        return None

    rates = api_data.get("data", {})
    brl_rate = rates.get("BRL")
    eur_rate = rates.get("EUR")

    if brl_rate is None or eur_rate is None:
        print(f"Error: Missing 'BRL' ({brl_rate}) or 'EUR' ({eur_rate}) rate in API data.")
        return None

    try:
        # Convert rates to float, handling potential errors
        real_value = float(brl_rate)
        euro_value = float(eur_rate)

        # Create a Currency object (timestamp uses UTC)
        currency_obj = Currency(
            Real=real_value,
            Euro=euro_value,
            timestamp=datetime.now() # Use UTC for consistency
        )
        print(f"Data transformed successfully: Real={real_value}, Euro={euro_value}")
        return currency_obj

    except (ValueError, TypeError) as e:
        print(f"Error converting rates to float: {e}. Rates received: BRL={brl_rate}, EUR={eur_rate}")
        return None

