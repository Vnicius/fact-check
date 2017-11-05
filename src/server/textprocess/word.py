#!/usr/bin/python3
# -*- coding:utf-8 -*-

class Word:
    def __init__(self, word, word_class):
        self.word = word
        self.synonyms = []
        self.word_class = word_class
    
    def __str__(self):
        return "Palavra: " + self.word + "\n" \
                + "Classe: " + self.word_class + "\n" \
                + "Sinonimo: " + str(self.synonyms) + "\n"