#!/usr/bin/python3
# -*- coding:utf-8 -*-

class Snippet:
    '''
    Class with main informations of a snippet
    '''
    def __init__ (self, _id, title, text, url):
        self._id = _id
        self.title = title
        self.text = text
        self.url = url
        self.correct = False
        self.incorrect = False
    
    def __repr__(self):
        return "\nId: " + str(self._id) \
                + "\nTitle: " + self.title \
                + "\nText: " + self.text \
                + "\nURL: " + self.url \
                + "\nCorrect: " + str(self.correct) \
                + "\nIncorrect: " + str(self.incorrect)
    
    def __dict__(self):
        return {"_id" : self._id, "title" : self.title,
                "text" : self.text, "url" : self.url,
                "correct" : self.correct, "incorrect" : self.incorrect}