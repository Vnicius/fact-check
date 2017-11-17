#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
import re
from bs4 import BeautifulSoup
from textprocess.word import Word
from textprocess.verb import Verb

VERB_REGEX = re.compile(r'.* vem do verbo (.*)\. .*')

class QueryWords:

    def __init__(self):
        self.site = 'https://www.dicio.com.br/'
        self.soup = None
    
    def query(self, word):
        '''
        Return a object of Word with extra informations
        '''
        query_word = word.word        

        try:
            r = requests.get(self.site + query_word)
            self.soup = BeautifulSoup(r.text, "lxml")
        except:
            return word

        self.__get_synonyms(word)

        if word.word_class == "V":
            self.__get_infinitive_verbo(word)
        
        return word

    def __get_infinitive_verbo(self, word):

        infinitive = ""
        
        try:
            text_inf = self.soup.find("p", class_="significado intro-conjugacao").find("span").text
        except:
            return
        
        if text_inf:
            infinitive = VERB_REGEX.findall(text_inf)[0]

        word.infinitive = infinitive

    def __get_synonyms(self, word):
        synonyms = []
        try:
            words = self.soup.find("p", class_="adicional sinonimos").find_all("a")
            for w in words:
                synonyms.append(w.text)

        except AttributeError:
            return []

        word.synonyms = synonyms

if __name__ == "__main__":
    import sys

    print (QueryWords().query(sys.argv[1]))