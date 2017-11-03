#!/usr/bin/python3
# -*- coding:utf-8 -*-

from flask import Flask, request
from flask_cors import CORS
import json
#import time

app = Flask(__name__)
CORS(app)

@app.route("/snippets", methods = ['POST'])
def get_snippets():
    #print (request.get_json()["text"])
    with open("teste.json") as js:
        #print(js.read())
        #time.sleep(1)
        return js.read()

@app.route("/send", methods=['POST'])
def send_db():
    #print(json.dumps(request.get_json()))
    return "ok"

if __name__ == "__main__":
    app.run(debug=True)