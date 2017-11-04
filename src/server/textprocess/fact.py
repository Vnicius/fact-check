#!/usr/bin/python3
# -*- coding:utf8 -*-

class Fact:
    def __init__(self, _id, claim, matches, snippets):
        self._id = _id
        self.claim = claim
        self.matches = matches
        self.snippets = snippets
    
    def __dict__(self):
        return {"_id" : self._id, "claim" : self.claim,
                "matches" : self.matches, "snippets" : [snip.__dict__() for snip in self.snippets]}