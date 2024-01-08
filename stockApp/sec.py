import requests
from bs4 import BeautifulSoup
import json
import os

# Print the current working directory
print("Current Working Directory: ", os.getcwd())

# Specify the path to your JSON file
file_path = 'stocks/stockApp/data/company_tickers.json'

# Open the file and load its contents
try:
    with open(file_path, 'r') as file:
        data = json.load(file)

        # Check if data is a list or a dictionary and handle accordingly
        if isinstance(data, list):
            # If it's a list, take the first 10 items
            first_10_items = data[:10]
        elif isinstance(data, dict):
            # If it's a dictionary, take the first 10 key-value pairs
            first_10_items = dict(list(data.items())[:10])
        else:
            print("JSON is neither a list nor a dictionary")
            first_10_items = {}

        # Print the first 10 items
        print(json.dumps(first_10_items, indent=4))

except FileNotFoundError:
    print(f"File not found: {file_path}")
except json.JSONDecodeError:
    print("Error decoding JSON")

#url = f'https://www.sec.gov/edgar/browse/?CIK=cik'

#def get_cik(company_name):
    # SEC's EDGAR search URL for company CIK
    #url = f'https://www.sec.gov/cgi-bin/browse-edgar?company={company_name}'

    # Send HTTP request to the SEC website
    #response = requests.get(url)
    #if response.status_code != 200:
    #    return "Error: Unable to retrieve data"

    # Parse the HTML content
    #soup = BeautifulSoup(response.text, 'html.parser')

    # Find the CIK number in the parsed HTML
    # The exact method depends on how the SEC's website structures the information
    #cik_tag = soup.find('span', class_='companyName').find_next('a')
    #if cik_tag:
    #    cik = cik_tag.text.strip()
    #    return cik
    #else:
    #    return "CIK not found"

# Get CIK for Apple Inc.
#apple_cik = get_cik("Apple Inc")
#print(apple_cik)