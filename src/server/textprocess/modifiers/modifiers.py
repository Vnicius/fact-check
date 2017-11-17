#!/usr/bin/python3
# -*- codign:utf-8 -*-

from textprocess.modifiers.synonymmodifier import SynonymModifier
from textprocess.modifiers.inverserordermodifier import InverseOrderModifier

class Modifiers():
    def __init__(self, pivot):
        self.modifiers = [SynonymModifier(1), SynonymModifier(2), InverseOrderModifier(pivot)]
    
    def get_modifiers(self):
        return self.modifiers
