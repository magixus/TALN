from django.utils.encoding import force_bytes
import requests
import bs4
import itertools
import json

def kamouss(word):
    res = requests.get('https://www.almaany.com/ar/dict/ar-ar/'+word+'/')
    bs = bs4.BeautifulSoup(res.text, 'html.parser')
    lines = bs.select('.meaning-results')
    x = lines[0].getText().split('\n')
    
    xy = []
    dictio = {}
    
    for y in x:
       if (y is not ''):
          xy.append(y)

    dictio = dict(itertools.zip_longest(*[iter(xy)] * 2, fillvalue=""))

    return dictio