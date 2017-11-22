#!/usr/bin/python3
# -*- coding:utf-8 -*-

from textprocess.modifiers.synonymmodifier import SynonymModifier
from textprocess.modifiers.indirectordermodifier import IndirectOrderModifier

class SynonymIndirectModifier:
    '''
    Class to apply the synonym and indirect approaches
    '''
    def __init__(self, pivot, probability=1):
        '''
        Params
        ---
        pivot: to indirect order modifier
        probability: to synonym mofier
        '''
        self.pivot = pivot
        self.probability = probability
    
    def modify_sentence(self, words):
        '''
        Apply synonym and invert modifiers
        '''
        synonym = SynonymModifier(self.probability).modify_sentence(words)
        
        return IndirectOrderModifier(self.pivot).modify_sentence(synonym)
