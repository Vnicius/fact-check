#!/usr/bin/python3
# -*- coding:utf-8 -*-

from copy import deepcopy

class SynonymModifier():
    def __init__(self, synonym_number=1):
        self.synonym_number = synonym_number

    def modify_sentence(self, words):
        aux = deepcopy(words)
        no_replaces = True

        for word in aux:
            if len(word.synonyms) >= self.synonym_number:
                word.word = word.synonyms[self.synonym_number - 1]
                no_replaces = False

        if no_replaces:
            return []
        
        return aux