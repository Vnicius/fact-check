#!/usr/bin/python3
# -*- coding:utf8 -*-

from textprocess.word import Word

class Verb(Word):
    def __init__(self, word, word_class):
        super(Verb, self).__init__(word, word_class)
        self.infinitive = ""
    
    def __str__(self):
        return super(Verb, self).__str__() + "Infinitivo: " + self.infinitive + "\n"
 