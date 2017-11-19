#!/usr/bin/python3
# -*- coding:utf-8 -*-

from copy import deepcopy
from textprocess import Word

class IndirectOrderModifier():
    '''
    Class to make a sentence in indirect order
    '''
    def __init__(self, pivot):
        '''
        Params
        ---
        pivot: is the index that nominal and verbal parts
        '''
        self.pivot = pivot + 1

    def modify_sentence(self, words):
        '''
        Return a text in indirect order

        Params
        ---
        words: a list of objects 'Word'
        '''
        aux = deepcopy(words)
        pu = Word("","")

        start = aux[self.pivot:]
        end = aux[:self.pivot]

        if start[-1].word in ".?!":
            pu = start[-1]
            start = start[:-1]

        if start[0].word[0].isalpha():
            lst = list(start[0].word)

            lst[0] = lst[0].upper()
            start[0].word = "".join(lst)

        if end[0].word_class != "NPROP":
            lst = list(end[0].word)
            lst[0] = lst[0].lower()
            end[0].word = "".join(lst)

        return start + end + [pu]
