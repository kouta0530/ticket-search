# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 18:52:51 2019

@author: kouta
"""

import requests
from bs4 import BeautifulSoup
import json

link = "https://eplus.jp/sf/search?block=true&keyword="
link2 = "https://t.livepocket.jp/event/search?word="
link3 = "https://ticket.st/artists/"
#url = 'https://eplus.jp/sf/word/0000118837'

def inputSite():
    key = input()
    site = link + key
    return site

def search_e_plus(word):
# レスポンスの HTML から BeautifulSoup オブジェクトを作る
    list = []
    res = requests.get(link + word)
    soup = BeautifulSoup(res.text, 'html.parser')

    title_text = soup.find('title').get_text()
    print(title_text)
    a = soup.find_all("script",{"class":"json"})
    a = json.loads(a[0].get_text().encode('utf-8')) 
    a = a["data"]
    a = a["record_list"]
    
    #key = a[0].items()
    #print(key)
    
    for t in range(len(a)): 
        datas = {"name" :a[t]["kanren_kogyo_sub"]["kogyo_name_1"],"info":a[t]["koenbi_term"],
        "venue":a[t]["kanren_venue"]["venue_name"]}
        
        list.append(datas)
    
    return list

def search_live_pocket(word):
    res = requests.get(link2 + word)
    soup = BeautifulSoup(res.text, 'html.parser')
    title_text = soup.find('title').get_text()
    print(title_text)
    a = soup.find_all('h3')
    date = soup.find_all('ul',{"class": "info"})
        
    
    name = [t.get_text() for t in a]
    dates = [t.find("li").get_text()for t in date]
    venue = [t.find_all("span")[1].get_text() for t in date]
    
    list =[]
    
    for t in range(len(name)):
        datas = {"name": name[t],"info":dates[t],"venue":venue[t]}
        list.append(datas)
    
    return list

def search_street(word):
    res = requests.get(link3 + word + "-tickets?utm_content=search")
    soup = BeautifulSoup(res.text, 'html.parser')
    title_text = soup.find('title').get_text()
    
    date = soup.find_all("li",{"class":"date"})
    title = soup.find_all("li",{"class":"artist"})

    title = [t.get_text() for t in title]
    date = [t.get_text() for t in date]
    
    list = []
    for t in range(len(date)):
        datas = {"name": title[t],"info":date[t]}
        list.append(datas)

    return list
    

def search_cluster():
    res = requests.get("https://cluster.mu/events")
    res.encoding = res.apparent_encoding
    soup = BeautifulSoup(res.text, 'html.parser')

    print(soup.find_all("script"))
    return 0
