#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
import re
from textprocess.word import Word as Word
from bs4 import BeautifulSoup

VERBO_REGEX = re.compile(r'.* vem do verbo (.*)\. .*')

class QueryWords:

    def __init__(self):
        self.site = 'https://www.dicio.com.br/'
        self.soup = None
        self.__word = Word()
    
    def query(self, palavra):
        self.__word.palavra = palavra
        try:
            r = requests.get( self.site + palavra)
            self.soup = BeautifulSoup(r.text, "lxml")
        except:
            return self.__word

        self.__get_sinonimos()
        self.__get_infinitivo_verbo()
        
        ret = self.__word
        self.__word = Word()

        return ret

    def __get_infinitivo_verbo(self):

        infinitivo = ""
        
        try:
            texto_inf = self.soup.find("p", class_="significado intro-conjugacao").find("span").text
        except:
            return
        
        if texto_inf:
            infinitivo = VERBO_REGEX.findall(texto_inf)[0]

        self.__word.infinitivo = infinitivo

    def __get_sinonimos(self):
        sinonimos = []
        try:
            palavras = self.soup.find("p", class_="adicional sinonimos").find_all("a")

            for palavra in palavras:
                sinonimos.append(palavra.text)

        except AttributeError:
            return []

        self.__word.sinonimos = sinonimos

if __name__ == "__main__":
    import sys

    print (QueryWords().query(sys.argv[1]))