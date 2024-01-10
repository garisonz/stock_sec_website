import requests
from bs4 import BeautifulSoup
import json
import urllib.request
import lxml
import unicodedata
import re

# json parse 

def restore_windows_1252_characters(restore_string):
    """
        Replace C1 control characters in the Unicode string s by the
        characters at the corresponding code points in Windows-1252,
        where possible.
    """

    def to_windows_1252(match):
        try:
            return bytes([ord(match.group(0))]).decode('windows-1252')
        except UnicodeDecodeError:
            # No character at the corresponding code point: remove it.
            return ''
        
    return re.sub(r'[\u0080-\u0099]', to_windows_1252, restore_string)

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
# https://data.sec.gov/api/xbrl/companyconcept/CIK0000{cik}/us-gaap/AccountsPayableCurrent.json
url = 'https://data.sec.gov/api/xbrl/companyconcept/CIK0000789019/us-gaap/AccountsPayableCurrent.json'

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
    list = []
    list = json_data['units'].get('USD')

    last_item = len(list)
    i = len(list)-1

    # prints all 10k

    #filings = []

    #while i > 0:
    #    if list[0:last_item][i].get('form') == '10-K':
    #        print(list[0:last_item][i])
    #        filings.append(list[0:last_item][i])
    #        i -= 1
    #        continue
        
    #    i -= 1

    # prints the most recent 10k & 10q

    while i > 0:
        if list[0:last_item][i].get('form') == '10-K':
            print(list[0:last_item][i])
            break
        
        i -= 1
    
    while i > 0:
        if list[0:last_item][i].get('form') == '10-Q':
            print(list[0:last_item][i])
            break
        
        i -= 1

# 'https://www.sec.gov/Archives/edgar/data/{cik}/{accn no -}/{accn}.txt'
        
weburl = 'https://www.sec.gov/Archives/edgar/data/789019/000095017023035122/0000950170-23-035122.txt'

page = requests.get(weburl, headers=headers)

print("HTTP Status Code:", page.status_code)

# Check if the request was successful
if page.status_code == 200:

    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(page.content, 'lxml')

    v = soup.find('sec-header')
    print(v.get_text())

    for tag in soup.find_all(True):
        print(tag.name)

    z = soup.find('document')
    content = z.get_text()
    content = content.strip()
    content = ''.join(content.split())
    file_path = 'stocks\stockApp\output.txt'

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

    

    
    
    

else:
    print("Failed to fetch the web page")