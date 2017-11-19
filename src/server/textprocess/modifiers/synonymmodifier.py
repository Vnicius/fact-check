#!/usr/bin/python3
# -*- coding:utf-8 -*-

from copy import deepcopy

class SynonymModifier():
    '''
    Class to change the words by him synonyms
    '''
    def __init__(self, synonym_number=1):
        '''
        Params
        ---
        synonym_number: the synonym in the array of synonyms in the each object 'Word' 
        '''
        self.synonym_number = synonym_number

    def modify_sentence(self, words):
        '''
        Return the setence with the synonym words

        Params
        ---
        words: list of objects 'Word'
        '''
        aux = deepcopy(words)
        no_replaces = True

        for word in aux:
            if len(word.synonyms) >= self.synonym_number:
                word.word = word.synonyms[self.synonym_number - 1]
                no_replaces = False

        if no_replaces:
            return []
        
        return aux