#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import requests
from BeautifulSoup import BeautifulSoup

phones = [
'apple-iphone6s-16Go-argent',
'apple-iphone6-plus-16go-or',
'samsung-galaxy-note7-noir'
 ]
base_url = 'http://shop.sosh.fr/mobile/'
def handleAvailable(phone):
    print phone + ' est disponible'

def handleUnAvailable(phone):
    print phone + ' est indisponible'
def handlePreOrder(phone):
    print phone + ' est disponible en précommande'

for phone in phones:
    url = base_url + phone
    response = requests.get(url)
    html = response.content
    soup = BeautifulSoup(html)
    stock = soup.find('span', attrs={'id': 'SPAN_Stock'})
    if stock == None:
         handleUnAvailable(phone)
    else:
        if "En stock" in stock.text:
            handleAvailable(phone)
        else:
            handlePreOrder(phone)
