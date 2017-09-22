#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 11:44:40 2017

@author: miyashitayudai
"""
import requests
import shutil
from urllib import request
from bs4 import BeautifulSoup
import os

def download_img(url, file_name):
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        with open(file_name, 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)

# ガッキーの画像を検索
query = "新垣結衣"
label="0"
query= query.split()
query='+'.join(query)
url="https://www.google.co.in/search?q="+query+"&source=lnms&tbm=isch"

# page = open('tower.html', 'r').read()
page = requests.get(url).text
DIR = "a_gacky"
soup = BeautifulSoup(page, 'html.parser')

saveCount = 0
for raw_img in soup.find_all('img'):
  link = raw_img.get('src')
  if link:
      saveCount = saveCount + 1
      download_img(link, DIR  + "/" + "{0:04d}".format(saveCount) + ".png")
      #download(link)