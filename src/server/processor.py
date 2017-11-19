#!/usr/bin/python3
# -*- coding:utf-8 -*-

from textprocess import bingsearch
from textprocess import GoogleSearch
from textprocess import Fact
from textprocess import SentenceGenerator
from dao import FactsDb
import json

factsDb = FactsDb()

def process(claim):
    '''
    Process the claim returning a list of snippets on the web
    '''
    sentences = SentenceGenerator().generate_sentences(claim)
    facts = []
    matches = 0
    snippets = []
    ret = "{\"response\":["

    for index, sentence in enumerate(sentences):
        matches, snippets = GoogleSearch().search(sentence)

        retDB = __check_db(sentence)

        if retDB:
            retDB["_id"] = str(retDB["_id"])
            facts.append(retDB)
            continue

        idFact = __save_db(Fact(sentence, matches, snippets))

        factJson = __get_fact(idFact)

        if factJson:
            factJson["_id"] = str(factJson["_id"])
            facts.append(factJson)
            continue

        # facts.append(Fact(index + 1, sentence,
        #                   matches, snippets))

    for index, fact in enumerate(facts):
        if index != len(facts)-1:
            ret += json.dumps(fact) + ","
        else:
            ret += json.dumps(fact) + "]}"

    return ret

def __check_db(claim):
    return factsDb.find(claim)

def __save_db(fact):
    return factsDb.save(fact.__dict__())

def __get_fact(_id):
    return factsDb.find_by_id(_id)

def update_db(values):
    factsDb.update(values)
