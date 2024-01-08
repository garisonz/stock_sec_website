# cd Projects/stockWeb/stocks/
# git add .
# git commit -am "msg"
# git push

from django.shortcuts import render, redirect
from sec_api import ExtractorApi, QueryApi
from .models import *
from .forms import StockForm
from django.contrib import messages
import requests
import json
import xml.etree.ElementTree as ET
from django.http import JsonResponse

def home(request):
    return render(request, 'home.html', {})

def landing(request):
    if request.method == 'POST':
        ticker = request.POST['ticker']
        api_request = requests.get("https://www.alphavantage.co/query?function=OVERVIEW&symbol=" + ticker + "&apikey=FF1G5XBIZXLG4C9Z")
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error"

        return render(request, 'landing.html', {'api': api})
    else:
       return render(request, 'landing.html', {'ticker': 'Enter a Ticker Symbol'})
    

def about(request):
    return render(request, 'about.html', {})

def learn(request):
    return render(request, 'learn.html', {})

def portfolio(request):

    if request.method == 'POST':
        form = StockForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, ("Stock Has Been Added"))
            return redirect('portfolio')
    else:
        ticker = Stock.objects.all()
        return render(request, 'portfolio.html', {'ticker': ticker})

def delete(request, stock_id):
    item = Stock.objects.get(pk=stock_id)
    item.delete()
    messages.success(request, ("Stock Has Been Deleted"))
    return redirect(portfolio)


def tenk(request):
    return render(request, '10k.html', {})

def tenq(request):
    return render(request, '10q.html', {})

def eightk(request):
    return render(request, '8k.html', {})

def test(request):

    header = {
        "User-Agent": "garisonzag88@gmail.com"
    }

    stock = Stock_info.objects.get(ticker="AAPL")

    stock_cik = stock.cik_str

    return render(request, 'test.html', {'stock_cik': stock_cik})

def fetch_filings(feed_url, headers):
    
    response = requests.get(feed_url, headers=headers)
    response.raise_for_status()

    # Parse the XML response
    root = ET.fromstring(response.content)
    filings = []
    for item in root.findall('./channel/item'):
        filings.append({
            'title': item.find('title').text,
            'link': item.find('link').text,
            # Add other relevant information here
        })

    return filings

def filings_view(request):
    
    headers = {
        'User-Agent': '(garisonzag88@gmail.com)'
    }

    feed_url = 'https://www.sec.gov/cgi-bin/browse-edgar?action=getcurrent&CIK=&type=10-K&company=&dateb=&owner=exclude&start=0&count=40&output=atom'
    filings = fetch_filings(feed_url, headers)

    return render(request, 'test.html', {'filings': filings})

def latest(request):
    return render(request, 'latest.html', {})