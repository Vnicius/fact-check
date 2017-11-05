#!/usr/bin/python3
# -*- coding:utf-8 -*-

from textprocess.tagger import Tagger
from textprocess.word import Word
from textprocess.verb import Verb
from textprocess.querywords import QueryWords

# from tagger import Tagger
# from word import Word
# from verb import Verb
# from querywords import QueryWords

def generator(start_claim):
    if start_claim[0] == "\"":
        start_claim = start_claim[1:]
        
    if start_claim[-1] == "\"":
        start_claim = start_claim[:-1]

    result = __claim_set(start_claim)
    return result

def __array2sentence(array_words):
    result = ""

    for word in array_words:
        result += word.word + " "
    
    result = result[:-1]

    return result

def __claim_set(start_claim):
    tagged = __tag(start_claim)
    words_set = __words_set(tagged)
    qw = QueryWords()
    claim_set = [start_claim]
    
    for word in words_set:
        if word.word_class in ["V", "N", "ADJ"]:
            word = qw.query(word)

    for word in words_set:
        if word.synonyms:
            word.word = word.synonyms[0]
    
    claim_set.append(__array2sentence(words_set))

    return claim_set

def __tag(text):
    return Tagger().tag(text)

def __words_set(tagged_text):
    words = []

    for word in tagged_text:
        if word[1] == "V":
            words.append(Verb(word[0],word[1]))
        else:
            words.append(Word(word[0],word[1]))

    return words

if __name__ == "__main__":
    import sys

    print(__claim_set(sys.argv[1]))