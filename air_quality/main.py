import os
from pprint import pprint
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the API token from the environment variables
api_token = os.getenv("AIR_QUALITY_API_TOKEN")

# Check if API token is available
if api_token is None:
    raise ValueError("API_TOKEN is not set in the .env file")

# URL for the API request
url = "https://api.waqi.info/feed/here/?token=" + api_token

# Make the API request
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    json_data = response.json()

    # Now you can work with the json_data as needed
    pprint(json_data)
else:
    # Print an error message if the request was not successful
    print(f"Error: {response.status_code} - {response.text}")
