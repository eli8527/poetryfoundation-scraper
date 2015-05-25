"""
PoetryFoundation Scraper

Simple web scraper that scrapes a poet's poems from the PoetryFoundation
website into a single txt file.

Eric Li
"""

from __future__ import print_function
from bs4 import BeautifulSoup
import urllib2
import re
import HTMLParser

poet = raw_input('Enter a poet: ')

poet = poet.lower()
poet = re.sub('[^a-z]+','-',poet)

fileout = poet + ".txt"
output = open(fileout,'w')

url = "http://www.poetryfoundation.org/bio/"+poet+"#about"
page = urllib2.urlopen(url)
soup = BeautifulSoup(page.read())
parser = HTMLParser.HTMLParser()

poems = soup.find_all('a',href=re.compile('.*/poetrymagazine/browse/.*'))
poems2 = soup.find_all('a',href=re.compile('.*/poem/.*'))

poems.extend(poems2)

for poem in poems:


    poemURL = 'http://www.poetryfoundation.org' + poem.get('href')
    poemPage = urllib2.urlopen(poemURL)
    poemSoup = BeautifulSoup(poemPage.read())
    
    poemTitle = poemSoup.find('div',{'id':'poem-top'})
    
    if poemTitle:
        print(parser.unescape(poemTitle.text).encode('utf8'),file=output)
        
        poemContent = poemSoup.find_all('div',{'class':'poem'})
        
        for line in poemContent:
            text = parser.unescape(line.text)
            out = text.encode('utf8')
            print(out,file=output)
        
