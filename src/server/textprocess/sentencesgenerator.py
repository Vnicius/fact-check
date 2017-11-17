#!/usr/bin/python3
# -*- coding:utf-8 -*-

import os

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

        sentences = self.__divide_sentences(start_claim)
        claim_sets = []
        final_claim_set = []
        claim = []

        for sentence in sentences:
            claim_sets.append(self.__claim_set(sentence))

        for index,_ in enumerate(claim_sets[0]):
            try:
                for index_claim, _ in enumerate(claim_sets):
                    claim.append(claim_sets[index_claim][index])
                
                final_claim_set.append(" ".join(claim))
                claim = []
            except IndexError:
                break

        return final_claim_set

    def __divide_sentences(self, start_claim):
        sentences = []
        sentence = []
        pronoms = self.__read_pronomes()
        
        for value in start_claim.split(" "):
            sentence.append(value)

            if "." in value:
                if value.lower() not in pronoms:
                    sentences.append(" ".join(sentence))
                    sentence = []
        
        if sentence:
            sentences.append(" ".join(sentence))
        
        return sentences

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
    
    def __read_pronomes(self):
        with open(os.path.dirname(os.path.realpath(__file__))+"/pronomesTratamento.csv") as pron:
            lines = pron.readlines()
            pronoms = []

            for line in lines:
                pronoms.append(line.replace("\n",""))
            
            return pronoms
    
if __name__ == "__main__":
    import sys

    print(SentenceGenerator().generate_sentences(sys.argv[1]))