#!/usr/bin/python3
# -*- coding : utf-8 -*-

import os
import nlpnet

class Tagger:
    '''
    POS-Tagger for portuguese language
    '''
    def __init__(self):
        self.tagger = nlpnet.POSTagger(os.path.dirname(os.path.realpath(__file__)) + "/pos-pt", language="pt")

    def tag(self, text):
        '''
        Return the tagged text
        '''
        return self.tagger.tag(text)[0]

if __name__ == "__main__":
    import sys

    print(Tagger().tag(sys.argv[1]))