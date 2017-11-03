#!/usr/bin/python3
# -*- coding:utf-8 -*-

from pymongo import MongoClient

class FactsDb:
    def __init__(self):
        self.db = MongoClient("mongodb://localhost:27017/").factcheck.facts
    
    def save(self, data):
        self.db.insert(data)