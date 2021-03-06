#!/usr/bin/python3
# -*- coding:utf8 -*-

class Fact:
    '''
    Class to group extra informations about the set of snippets
    '''
    def __init__(self, claim, matches, snippets):
        #self._id = _id
        self.claim = claim
        self.matches = matches
        self.snippets = snippets

    def __dict__(self):
        return {"claim" : self.claim,
                "matches" : self.matches,
                "snippets" : [snip.__dict__() for snip in self.snippets]}
