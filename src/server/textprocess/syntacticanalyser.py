#!/usr/bin/python3
# -*- coding:utf-8 -*-

class SyntacticAnalyser:
    def __init__(self):
        self.words = None
        self.current_index = 0

    def __next(self):
        aux = self.words[self.current_index]
        self.current_index += 1
        
        return aux
    
    def __back(self):
        self.current_index -= 1
        return self.words[self.current_index]

    def start(self, words):
        self.words = words
        self.__S()

    def __S(self):
        if self.__NP():
            if not self.__VP():
                return False

        elif self.__VP():
            self.__NP()

        elif self.__ADVP():
            if not self.__S():
                return False

        return True
    
    def __NP(self):
        if self.__next()[1] in ["ART", "PROSUB", "NUM"]:
            if self.__N_ln():
                return True
            else:
                return False

        else:
            self.__back()
        
        if self.__next()[1] == "PROADJ":
            if self.__N_ln():
               return True
            elif self.__NP():
                return True
            else:
                return False
        else:
            self.__back()
        
        if self.__N_ln():
            return True
        else:
            return False
    
    def __N_ln(self):
        if "PRO" in self.__next()[1]:
            if self.__N_lnln():
                return True
            else:
                return False
        else:
            self.__back()
        
        if self.__next()[1] in ["N", "NPROP"]:
            if self.__N_lnln():
                return True
            else:
                return False
        else:
            self.__back()
        
        if self.__AP():
            if self.__N_ln():
                return self.__N_lnln()
        else:
            return False

    def __N_lnln(self):
        if self.__AP():
            return self.__N_lnln()

        elif self.__PP():
            return self.__N_lnln()
        
        return True
        