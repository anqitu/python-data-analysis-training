# Q7
# Write a module that gets the news headlines from NTU news

from bs4 import BeautifulSoup
from urllib import request

URL = "http://news.ntu.edu.sg/Pages/NewsSummary.aspx?Category=News+Releases"

text_html = request.urlopen(URL).read()
soup = BeautifulSoup(text_html, 'html.parser')

news_container = soup.find('div', {'id': 'NTU_NewsSummaryListing'})
news_links = news_container.find_all('a')[:-2]
news_headlines = [n.text for n in news_links]
