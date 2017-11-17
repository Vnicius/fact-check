#!/usr/bin/python3
# -*- coding:utf-8 -*-

from copy import deepcopy

class InverseOrderModifier():
    def __init__(self, pivot):
        self.pivot = pivot + 1

    def modify_sentence(self, words):
        aux = deepcopy(words)

        start = words[self.pivot:]
        end = words[:self.pivot]
        
        if start[0].word[0].isalpha():
            lst = list(start[0].word)
            lst[0] = lst[0].upper()
            start[0].word = "".join(lst)
        
        if end[0].word_class != "NPROP":
            lst = list(end[0].word)
            lst[0] = lst[0].lower()
            end[0].word = "".join(lst)

        return start + end
