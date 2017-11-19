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
    '''
    Class to generate diferents versions of a sentence.
    '''

    def generate_sentences(self, start_claim):
        '''
        Return a list of modifieds sentences
        '''
        # remove quotation marks if they are used
        if start_claim[0] == "\"":
            start_claim = start_claim[1:]

        if start_claim[-1] == "\"":
            start_claim = start_claim[:-1]

        # devide the sentences of the claim
        sentences = self.__divide_sentences(start_claim)

        claim_sets = []
        final_claim_set = []
        claim = []

        # get the set of modifieds sentences for each sentence in the claim
        for sentence in sentences:
            claim_sets.append(self.__claim_set(sentence))

        # concat the modifieds sentences
        for index, _ in enumerate(claim_sets[0]):
            try:
                for index_claim, _ in enumerate(claim_sets):
                    claim.append(claim_sets[index_claim][index])

                final_claim_set.append(" ".join(claim))
                claim = []
            except IndexError:
                break

        return final_claim_set

    def __divide_sentences(self, start_claim):
        '''
        Devide the sentences of the claim by terminate punctuations
        and return as a list

        Params
        ---
        start_claim: the original text
        '''
        sentences = []
        sentence = []
        pronouns = self.__read_pronouns()

        # divide the sentences by terminate pontuations
        for value in start_claim.split(" "):
            sentence.append(value)

            if "." in value:
                # if the word is not a pronoun
                if value.lower() not in pronouns:
                    sentences.append(" ".join(sentence))
                    sentence = []

            elif "?!" in value:
                sentences.append(" ".join(sentence))
                sentence = []

        if sentence:
            sentences.append(" ".join(sentence))

        return sentences

    def __array2sentence(self, array_words):
        '''
        Return the sentence by a list o objects 'Word'

        Params
        ---
        array_words: a list of objects 'Word'
        '''
        result = ""

        for word in array_words:
            if word.word_class == "PU":
                result = result[:-1]
                result += word.word + " "
            else:
                result += word.word + " "

        result = result[:-1]

        return result

    def __claim_set(self, start_claim):
        '''
        Return different version of the original claim

        Params
        ---
        start_claim: the original text
        '''
        tagger = Tagger()   # POS-tagger for portuguese
        tagged_sentence = tagger.tag(start_claim)
        words_set = self.__words_set(tagged_sentence) # get the sentence as a list of objects 'Word'
        qw = QueryWords() # query extra informations of a word
        claim_set = [start_claim]
        analyser = SyntacticAnalyser() # syntactical analyser for portuguese sentences
        sentence_modifiers = None   # list of sentences modifiers
        aux_set = []    # auxiliar list
        aux_sentence = ""   # auxiliar string

        # analyze the syntax of the original sentence
        if not analyser.analysis(tagged_sentence):
            return []

        sentence_modifiers = Modifiers(analyser.pivot)

        # query extra informations of words with the tags 'V', 'N' and 'ADJ'
        for word in words_set:
            if word.word_class in ["V", "N", "ADJ"]:
                word = qw.query(word)

        # apply the modifiers in the original sentence
        for mod in sentence_modifiers.get_modifiers():
            aux_set = mod.modify_sentence(words_set)
            if aux_set:
                aux_sentence = self.__array2sentence(aux_set)

                # check if sytax of the modified sentence is correct
                if analyser.analysis(tagger.tag(aux_sentence)):
                    claim_set.append(aux_sentence)

        return claim_set

    def __words_set(self, tagged_text):
        '''
        Return a list of objects 'Word'

        Params
        ---
        tagged_text: the list o tuples with the word and his tag
        '''
        words = []

        for word in tagged_text:
            if word[1] == "V":
                words.append(Verb(word[0], word[1]))
            else:
                words.append(Word(word[0], word[1]))

        return words

    def __read_pronouns(self):
        '''
        Red the file of pronouns the portuguese language
        '''
        with open(os.path.dirname(os.path.realpath(__file__))+"/pronomesTratamento.csv") as pron:
            lines = pron.readlines()
            pronouns = []

            for line in lines:
                pronouns.append(line.replace("\n", ""))

            return pronouns
    
if __name__ == "__main__":
    import sys

    print(SentenceGenerator().generate_sentences(sys.argv[1]))
