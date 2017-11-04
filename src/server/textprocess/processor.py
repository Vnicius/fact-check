#!/usr/bin/python3
# -*- coding:utf-8 -*-

import textprocess.bingsearch as bingsearch
from textprocess.fact import Fact
import textprocess.sentencesgenerator as sentencesgenerator
import json

class Processor:
    def process(self, claim):
        sentences = sentencesgenerator.generator(claim)
        facts = []
        matches = 0
        snippets = []
        ret = "{\"response\":["

        for index, sentence in enumerate(sentences):
            matches, snippets = bingsearch.search(sentence)
            facts.append(Fact(index + 1, sentence,
                              matches, snippets))
        
        #print(json.dumps(facts[0].__dict__()))

        for index, fact in enumerate(facts):
            if index != len(facts)-1:
                ret += json.dumps(fact.__dict__()) + ","
            else:
                ret += json.dumps(fact.__dict__()) + "]}"
        #print(ret)

        return ret