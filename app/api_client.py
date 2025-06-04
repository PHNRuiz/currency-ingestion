# /home/ubuntu/currency-ingestion_refactored/currency-ingestion/app/api_client.py

import requests
from requests.exceptions import RequestException

BASE_URL = "https://api.freecurrencyapi.com/v1/latest"

def fetch_latest_rates(api_key: str) -> dict | None:
    """Fetches the latest currency exchange rates from the API.

    Args:
        api_key: The API key for accessing the service.

    Returns:
        A dictionary containing the API response data,
        or None if an error occurs during the request.
    """
    if not api_key:
        print("Error: API key cannot be empty.")
        return None

    params = {
        "apikey": api_key
        # Add other parameters if needed, e.g., "base_currency": "USD", "currencies": "EUR,BRL"
    }

    try:
        print(f"Requesting data from: {BASE_URL}")
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status() # Raises HTTPError for bad responses (4xx or 5xx)

        print("Successfully fetched data from API.")
        return response.json() # Return the parsed JSON data

    except RequestException as e:
        print(f"Error during API request to {BASE_URL}: {e}")
        return None # Return None to indicate failure

