# https://www.investopedia.com/articles/fundamental-analysis/08/sec-forms.asp#toc-form-8-k
# 880e695a62b65a8ed6191eeb3650f3e219f99eede29037143bd41ed6369db07d

from sec_api import ExtractorApi
from IPython.display import display, HTML
import pandas as pd

API_KEY = 'YOUR_API_KEY'

extractorApi = ExtractorApi('880e695a62b65a8ed6191eeb3650f3e219f99eede29037143bd41ed6369db07d')
filing_10_k_url = 'https://www.sec.gov/Archives/edgar/data/1318605/000156459021004599/tsla-10k_20201231.htm'

# helper function to pretty print long, single-line text to multi-line text
def pprint(text, line_length=100):
  words = text.split(' ')
  lines = []
  current_line = ''
  for word in words:
    if len(current_line + ' ' + word) <= line_length:
      current_line += ' ' + word
    else:
      lines.append(current_line.strip())
      current_line = word
  if current_line:
    lines.append(current_line.strip())
  print('\n'.join(lines))

# extract text section "Item 1 - Business" from 10-K
item_1_text = extractorApi.get_section(filing_10_k_url, '1', 'text')

print('Extracted Item 1 (Text)')
print('-----------------------')
pprint(item_1_text[0:1500])
print('... cut for brevity')
print('-----------------------')

# extract HTML section "Item 1 - Business" from 10-K
item_1_html = extractorApi.get_section(filing_10_k_url, '1', 'html')

print('Extracted Item 1 (HTML)')
print('-----------------------')
display(HTML(item_1_html[0:3000]))
print('... cut for brevity')
print('-----------------------')

# extract the HTML version of section "Item 6 - Selected Financial Data"
item_6_html = extractorApi.get_section(filing_10_k_url, '6', 'html')
print('Extracted Item 6 (HTML)')
print('-----------------------')
display(HTML(item_6_html[0:1000]))
print('... cut for brevity')
print('-----------------------')

# read HTML table from a string and convert to dataframe
tables = pd.read_html(item_6_html)
# first table includes the financial statements
df = tables[0] 
# drop all columns with NaN values except if the first cell is not NaN
mask = (df.iloc[1:, :].isna()).all(axis=0)
financial_statements = df.drop(df.columns[mask], axis=1).fillna('')
print('Consolidated financial statements as dataframe:')
financial_statements