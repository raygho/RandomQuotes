import requests
import pandas as pd
import urllib.request
from bs4 import BeautifulSoup as bs
from random import randrange



authors = []
quotes = []
n = randrange(8)
rn = randrange(50)


def get_quotes(page_number):
    global url
    page_num = str(page_number)
    url = ('https://www.brainyquote.com/topics/random-quotes' + '_' + page_num) # make it dynamic pages
    page = requests.get(url)
    soup = bs(page.text, 'html.parser')
    quote_text = soup.find_all('div', attrs={'class': 'grid-item qb clearfix bqQt'})
    for i in quote_text:
        quote = i.text.strip().split('\n')[0] # get quotes
        author = i.find('a', attrs={'title': 'view author'}).text.strip() # get author
        quotes.append(quote)
        authors.append(author)
    
    #return quotes, authors, url

    print(quotes[rn], '\nThe author is', authors[rn])



get_quotes(n)
