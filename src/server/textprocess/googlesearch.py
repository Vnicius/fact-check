#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import requests
import re
from bs4 import BeautifulSoup
from snippet import Snippet

URL_REGEX = re.compile(r'/url\?q=(.*)&sa.*')

class GoogleSearch:

    def __init__(self):
        self.site = 'https://www.google.com.br/search?q='
        #self.mode = "&tbm=nws"
        self.mode = "&sorce=lmns"
        self.soup = None
    
    def search(self, text):    
        snippets = []
        try:
            r = requests.get(self.site + text.replace(" ","+") + self.mode)
            self.soup = BeautifulSoup(r.text, "lxml")
        except:
            return text
        
        cont_results = self.soup.body.find(id= "resultStats").text

        snippets = self.__get_snippets()
        
        return cont_results, snippets

    def __get_snippets(self):

        snnipets = []
        limit = 4
        results = self.soup.body.find_all("div", class_ = "g")
        
        for index, value in enumerate(results):
            try:
                aux = Snippet(  index + 30,
                                value.find("a").text,
                                value.find("span", class_ = "st").text,
                                URL_REGEX.findall(value.find("a")["href"])[0])
                snnipets.append(aux)
                
                if len(snnipets) == limit:
                    break
            except:
                continue
        
        return snnipets

if __name__ == "__main__":
    import sys

    print (GoogleSearch().search(sys.argv[1]))