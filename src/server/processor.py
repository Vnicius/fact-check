#!/usr/bin/python3
# -*- coding:utf-8 -*-

from textprocess import bingsearch
from textprocess import GoogleSearch
from textprocess import Fact
from textprocess import SentenceGenerator
import json


def process(claim):
    sentences = SentenceGenerator().generate_sentences(claim)
    facts = []
    matches = 0
    snippets = []
    ret = "{\"response\":["

    for index, sentence in enumerate(sentences):
        matches, snippets = GoogleSearch().search(sentence)
        facts.append(Fact(index + 1, sentence,
                            matches, snippets))

    for index, fact in enumerate(facts):
        if index != len(facts)-1:
            ret += json.dumps(fact.__dict__()) + ","
        else:
            ret += json.dumps(fact.__dict__()) + "]}"

    return ret