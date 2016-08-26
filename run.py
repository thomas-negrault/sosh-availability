#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import json
from BeautifulSoup import BeautifulSoup
from ConfigParser import SafeConfigParser

# LOAD CONFIGURATION
config = SafeConfigParser()
config.read('config.ini')
phones = json.loads(config.get("configuration","phones"))
base_url = config.get("configuration","base_url")

# DEFINE HANDLE FUNCTIONS
def handleAvailable(phone):
    print phone + ' est disponible'
def handleUnAvailable(phone):
    print phone + ' est indisponible'
def handlePreOrder(phone):
    print phone + ' est disponible en precommande'

# CHECK
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
