#!/usr/bin/python3
# -*- coding:utf-8 -*-

from textprocess.tagger import Tagger
from textprocess.word import Word
from textprocess.verb import Verb
from textprocess.querywords import QueryWords
from textprocess.syntacticanalyser import SyntacticAnalyser
from textprocess.modifiers import Modifiers

class SentenceGenerator():

    def generate_sentences(self, start_claim):
        if start_claim[0] == "\"":
            start_claim = start_claim[1:]

        if start_claim[-1] == "\"":
            start_claim = start_claim[:-1]

        result = self.__claim_set(start_claim)
        return result

    def __array2sentence(self, array_words):
        result = ""

        for word in array_words:
            result += word.word + " "

        result = result[:-1]

        return result

    def __claim_set(self, start_claim):
        tagger = Tagger()
        tagged_sentence = tagger.tag(start_claim)
        words_set = self.__words_set(tagged_sentence)
        qw = QueryWords()
        claim_set = [start_claim]
        analyser = SyntacticAnalyser()
        sentence_modifiers = None
        aux_set = []
        aux_sentence = ""

        if not analyser.analysis(tagged_sentence):
            return []
        
        sentence_modifiers = Modifiers(analyser.pivot)
        
        for word in words_set:
            if word.word_class in ["V", "N", "ADJ"]:
                word = qw.query(word)

        for mod in sentence_modifiers.get_modifiers():
            aux_set = mod.modify_sentence(words_set)
            if aux_set:
                aux_sentence = self.__array2sentence(aux_set)
                if analyser.analysis(tagger.tag(aux_sentence)):
                    claim_set.append(aux_sentence)

        return claim_set

    def __words_set(self, tagged_text):
        words = []

        for word in tagged_text:
            if word[1] == "V":
                words.append(Verb(word[0],word[1]))
            else:
                words.append(Word(word[0],word[1]))

        return words
    
if __name__ == "__main__":
    import sys

    #print(__claim_set(sys.argv[1]))