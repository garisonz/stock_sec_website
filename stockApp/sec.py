import requests
from bs4 import BeautifulSoup
import json

# https://data.sec.gov/submissions/CIK{cik}.json
# json parse 

def fetch_and_parse_json(url, headers):
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Will raise an HTTPError for bad requests (4xx or 5xx)

        return response.json()
    except requests.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")

# URL pointing to the SEC JSON data
url = 'https://data.sec.gov/submissions/CIK0000320193.json'

# Headers including a User-Agent
headers = {
    'User-Agent': 'garisonzag88@gmail.com'  # Replace with your app name and email
}

# Fetch and parse the JSON
json_data = fetch_and_parse_json(url, headers)

# Check if data is fetched successfully
if json_data:
    # The structure of JSON needs to be known to navigate it properly
    # Here's an example of how you might access the primaryDocument
    # Adjust the key access based on the actual structure of your JSON data
    recent_filings = json_data.get('filings', {}).get('recent', {})
    if 'primaryDocument' in recent_filings:
        primary_document = recent_filings['primaryDocument']
        print("Primary Document:", primary_document)
    else:
        print("Primary document not found in the JSON data.")