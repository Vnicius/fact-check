#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
import re
from bs4 import BeautifulSoup
from textprocess.word import Word
from textprocess.verb import Verb

VERB_REGEX = re.compile(r'.* vem do verbo (.*)\. .*')

class QueryWords:
    '''
    Search for meatdatas of a word in the site "Dicio"
    '''
    def __init__(self):
        self.site = 'https://www.dicio.com.br/'
        self.soup = None

    def query(self, word):
        '''
        Return a object of 'Word' with extra informations

        Params
        ---
        word: A object 'Word' with the word that will be quered
        '''
        query_word = word.word

        try:
            # make the request by the html
            r = requests.get(self.site + query_word)
            # using to manipulate the html more easily
            self.soup = BeautifulSoup(r.text, "lxml")
        except:
            return word

        # get the list of synonyms of the word
        self.__set_synonyms(word)

        # get the infinitive form of a verb
        if word.word_class == "V":
            self.__get_infinitive_verb(word)

        return word

    def __get_infinitive_verb(self, word):
        '''
        Return the infinitive of a verb.
        '''
        infinitive = ""

        try:
            text_inf = self.soup.find("p", class_="significado intro-conjugacao").find("span").text
        except:
            return

        if text_inf:
            infinitive = VERB_REGEX.findall(text_inf)[0]

        word.infinitive = infinitive

    def __set_synonyms(self, word):
        '''
        Set the list of synonyms in the 'Word' object
        '''
        synonyms = []

        try:
            # looking for the synonyms
            words = self.soup.find("p", class_="adicional sinonimos").find_all("a")

            for w in words:
                synonyms.append(w.text)

        except AttributeError:
            return []

        word.synonyms = synonyms

if __name__ == "__main__":
    import sys

    print (QueryWords().query(sys.argv[1]))
