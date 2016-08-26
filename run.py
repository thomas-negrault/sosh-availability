#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import json
import time
import datetime
from BeautifulSoup import BeautifulSoup
from ConfigParser import SafeConfigParser
from pushbullet import Pushbullet

# DEFINE CONSTANTS
UNAVAILABLE = 0
PREORDER = 1
AVAILABLE = 2

# LOAD CONFIGURATION
global config
config = SafeConfigParser()
config.read('config.ini')
phones_links = json.loads(config.get("scrapper","phones"))
base_url = config.get("system","base_url")
phones = []
for phone_link in phones_links:
    phone = {
    "url": base_url + phone_link,
     "name": phone_link.replace("-", " "),
     "old_state": UNAVAILABLE,
     "current_state": UNAVAILABLE
      }
    phones.append(phone)

# DEFINE HANDLE FUNCTIONS
def notify(phone):
    date = datetime.datetime.now().strftime("%d %b %Y %H:%M")
    message = '[%s]%s is %s (was %s)' % (date, phone["name"], get_status_string(phone["current_state"]), get_status_string(phone["old_state"]))
    push_bullet_notify(message, phone["url"])
def get_status_string(state):
    if state == AVAILABLE:
        status = 'available'
    elif state == UNAVAILABLE:
        status = 'unavailable'
    else:
        status = 'in pre-order'
    return status
#DEFINE NOTIFICATION FUNCTIONS
def push_bullet_notify(message, link):
    pb = Pushbullet(config.get("notification","pushbullet_token"))
    try:
        pb.push_link(message, link)
    except Exception as ex:
        print ex.message

# CHECK
starttime=time.time()
interval = config.getfloat("scrapper","interval")
while True:
    for phone in phones:
        response = requests.get(phone["url"])
        html = response.content
        soup = BeautifulSoup(html)
        stock = soup.find('span', attrs={'id': 'SPAN_Stock'})
        if stock == None:
             state = UNAVAILABLE
        else:
            if "En stock" in stock.text:
                state = AVAILABLE
            else:
                state = PREORDER
        phone["old_state"] = phone["current_state"]
        phone["current_state"] = state
        if phone["current_state"] != phone["old_state"]:
            notify(phone)

    time.sleep(interval - ((time.time() - starttime) % interval))
