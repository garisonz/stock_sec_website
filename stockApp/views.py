# cd Projects/stockWeb/stocks/
# git add .
# git commit -am "msg"
# git push

from django.shortcuts import render, redirect
from sec_api import ExtractorApi, QueryApi
from .models import Stock
from .forms import StockForm
from django.contrib import messages
import requests
import json

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

def show_10k_filing(request):
    query_api = QueryApi(api_key="880e695a62b65a8ed6191eeb3650f3e219f99eede29037143bd41ed6369db07d")

    query = {
        "query": { 
           "query_string": { 
              "query": "ticker:AAPL AND formType:\"10-K\"" }},
        "from": "0",
        "size": "1",
        "sort": [{ "filedAt": { "order": "desc" } }]
    }

    filings = query_api.get_filings(query)
    filing_html = None

    if filings['filings']:
        filing_url = filings['filings'][0]['linkToFilingDetails']
        
        # Use ExtractorAPI to get the HTML content
        extractor_api_key = "880e695a62b65a8ed6191eeb3650f3e219f99eede29037143bd41ed6369db07d"
        extractor_response = requests.get("https://extractorapi.com/api/v1/extractor/?apikey={extractor_api_key}&url={filing_url}")
        
        if extractor_response.status_code == 200:
            filing_html = extractor_response.text
        else:
            # Handle errors or unsuccessful status codes
            filing_html = "Error fetching the document."

    return render(request, 'show_10k.html', {'filing_html': filing_html})