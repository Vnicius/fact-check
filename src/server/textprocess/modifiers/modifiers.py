#!/usr/bin/python3
# -*- codign:utf-8 -*-

from textprocess.modifiers.synonymmodifier import SynonymModifier
from textprocess.modifiers.indirectordermodifier import IndirectOrderModifier

class Modifiers():
    def __init__(self, pivot):
        self.modifiers = [SynonymModifier(1), SynonymModifier(2), IndirectOrderModifier(pivot)]

    def get_modifiers(self):
        return self.modifiers
