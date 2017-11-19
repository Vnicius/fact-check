#!/usr/bin/python3
# -*- coding:utf-8 -*-

from pymongo import MongoClient
from bson.objectid import ObjectId

class FactsDb:
    '''
    Save the snippets in the MongoDB
    '''
    def __init__(self):
        self.db = MongoClient("mongodb://localhost:27017/").factcheck.facts

    def save(self, data):
        return self.db.insert(data)

    def find(self, text):
        return self.db.find_one({"claim" : text})

    def find_by_id(self, _id):
        return self.db.find_one({"_id" : ObjectId(_id)})

    def update(self, facts):
        for fact in facts:
            fact["_id"] = ObjectId(fact["_id"])
            self.db.update({"_id" : fact["_id"]}, fact)

if __name__ == "__main__":
    print(FactsDb().find("teste"))
