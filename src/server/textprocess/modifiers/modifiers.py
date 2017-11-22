#!/usr/bin/python3
# -*- codign:utf-8 -*-

from textprocess.modifiers.synonymmodifier import SynonymModifier
from textprocess.modifiers.indirectordermodifier import IndirectOrderModifier
from textprocess.modifiers.synonymindirectmodifier import SynonymIndirectModifier

class Modifiers():
    def __init__(self, pivot):
        self.modifiers = [SynonymModifier(1),
                          SynonymModifier(0.5),
                          IndirectOrderModifier(pivot),
                          SynonymIndirectModifier(pivot, 0.7)]

    def get_modifiers(self):
        return self.modifiers
