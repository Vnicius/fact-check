# -*- coding: utf-8 -*-

import os
import http.client, urllib.parse, json
from textprocess.snippet import Snippet

# **********************************************
# *** Update or verify the following values. ***
# **********************************************

with open(os.path.dirname(os.path.realpath(__file__))+"/auth.in") as auth:
    subscriptionKey = auth.read()

# Verify the endpoint URI.  At this writing, only one endpoint is used for Bing
# search APIs.  In the future, regional endpoints may be available.  If you
# encounter unexpected authorization errors, double-check this value against
# the endpoint for your Bing Web search instance in your Azure dashboard.
host = "api.cognitive.microsoft.com"
path = "/bing/v7.0/search"

#term = "Microsoft Cognitive Services"

def search(term, quotes = True):
    "Performs a Bing Web search and returns the results."

    term = "\"" + term + "\""
    cont_matches = 0
    snippets = []

    headers = {'Ocp-Apim-Subscription-Key': subscriptionKey}
    conn = http.client.HTTPSConnection(host)
    query = urllib.parse.quote(term)
    conn.request("GET", path + "?q=" + query, headers=headers)
    response = conn.getresponse()
    
    try:
        results = json.loads(response.read().decode("utf8"))["webPages"]
        cont_matches = results["totalEstimatedMatches"]
        snippets = form_snippets(results["value"])
        if len(snippets) > 3:
            snippets = snippets[:3]
    except:
        return search(term, False)

    return cont_matches, snippets

def form_snippets(response):
    snippets = []

    for index, element in enumerate(response):
        snippets.append(Snippet(index + 30,
                                element["name"],
                                element["snippet"],
                                element["url"]))
    return(snippets)


if __name__ == "__main__":
    import sys
    term = sys.argv[1]
    search(term)