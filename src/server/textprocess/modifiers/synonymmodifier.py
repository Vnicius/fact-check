#!/usr/bin/python3
# -*- coding:utf-8 -*-

from copy import deepcopy
import random

class SynonymModifier():
    '''
    Class to change the words by him synonyms
    '''
    def __init__(self, probability=1):
        '''
        Params
        ---
        probability: the probability to change the the words by synonyms
        '''
        self.probability = probability

    def modify_sentence(self, words):
        '''
        Return the setence with the synonym words

        Params
        ---
        words: list of objects 'Word'
        '''
        aux = deepcopy(words)

        for word in aux:
            if random.random() < self.probability:
                if word.synonyms:
                    word.word = word.synonyms[random.randint(0, len(word.synonyms) - 1)]
        
        return aux