#!/usr/bin/python3
# -*- coding : utf-8 -*-

import nlpnet

class Tagger:
    def __init__(self):
        self.tagger = nlpnet.POSTagger("pos-pt", language="pt")

    def tag(self, text):
        return self.tagger.tag(text)

if __name__ == "__main__":
    import sys

    print(Tagger().tag(sys.argv[1]))