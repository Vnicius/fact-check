#!/usr/bin/python3
# -*- coding:utf-8 -*-

class Word:
    def __init__(self):
        self.palavra = ""
        self.sinonimos = []
        self.infinitivo = ""
        self.classe = ""
    
    def __str__(self):
        return "Palavra: " + self.palavra + "\n" \
                + "Classe: " + self.classe + "\n" \
                + "Sinonimo: " + str(self.sinonimos) + "\n" \
                + "Infinitivo: " + self.infinitivo