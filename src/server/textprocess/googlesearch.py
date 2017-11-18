#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import requests
import re
from bs4 import BeautifulSoup
from textprocess.snippet import Snippet

URL_REGEX = re.compile(r'/url\?q=(.*)&sa.*')

class GoogleSearch:
    '''
    Class to make searchs on Google and get some results in the first page.
    '''

    def __init__(self):
        self.base = 'https://www.google.com.br/search?q='
        #self.mode = "&tbm=nws"     # for results in the tab "news"
        self.mode = "&sorce=lmns"   # for general results
        self.soup = None
        self.__limit = 4

    def search(self, text):
        '''
        Search a text on Google e return the first results

        Params
        ---
        text: the text that will be searched
        '''

        snippets = []

        try:
            # make the request by the html
            r = requests.get(self.base + text.replace(" ", "+") + self.mode)
            # using to manipulate the html more easily
            self.soup = BeautifulSoup(r.text, "lxml")
        except:
            return text

        # get the count of total results founded by the Google
        cont_results = self.soup.body.find(id="resultStats").text

        # get the first snippets in the first page of results
        snippets = self.__get_snippets()

        return cont_results, snippets

    def __get_snippets(self):
        '''
        Get the first snippets of the results.
        '''
        snnipets = []
        # looking for the results
        results = self.soup.body.find_all("div", class_="g")

        # get the title, text and url by each snippet founded
        for index, value in enumerate(results):
            try:
                aux = Snippet(index + 30,
                              value.find("a").text,
                              value.find("span", class_="st").text,
                              URL_REGEX.findall(value.find("a")["href"])[0])
                snnipets.append(aux)

                # was delimited the number of snippets for each search
                if len(snnipets) == self.__limit:
                    break
            except:
                # ignore some results as videos and images
                # their tags are differents
                continue

        return snnipets

if __name__ == "__main__":
    import sys

    print (GoogleSearch().search(sys.argv[1]))
