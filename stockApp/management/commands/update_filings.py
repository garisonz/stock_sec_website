import feedparser
import datetime
from django.utils.dateparse import parse_date
from stockApp.models import Stock_info, Filing  # Replace 'myapp' with your actual app name

# SEC's RSS feed URL for latest 10-K filings
RSS_FEED_URL = "https://www.sec.gov/cgi-bin/browse-edgar?action=getcurrent&CIK=&type=10-K&company=&dateb=&owner=exclude&start=0&count=100&output=atom"

def update_filings():
    # Parse the RSS feed
    feed = feedparser.parse(RSS_FEED_URL)

    for entry in feed.entries:
        # Extract data from each entry
        filing_type = entry.title.split(' - ')[1]
        company_name = entry.title.split(' - ')[0]
        date_filed = parse_date(entry.updated)
        url = entry.link
        cik = entry.id.split('CIK=')[1][:10]  # Extract CIK from the entry ID

        # Ensure the company exists in the database, or create it
        company, created = Stock_info.objects.get_or_create(cik=cik, defaults={'name': company_name})

        # Create a new Filing record, if not already exists
        Filing.objects.get_or_create(
            company=company,
            filing_type=filing_type,
            date_filed=date_filed,
            accession_number=entry.id,  # Using entry ID as a unique identifier
            defaults={'url': url}
        )

if __name__ == "__main__":
    # Assuming you're running this script standalone, you need to set up Django environment
    import os
    import django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project.settings')  # Replace with your project's settings
    django.setup()

    # Update filings
    update_filings()
