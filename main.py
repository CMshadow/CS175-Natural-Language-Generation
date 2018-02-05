# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import nltk, re, pprint
from nltk import word_tokenize
from urllib import request
from bs4 import BeautifulSoup


"""
Tokenize a HTML
"""

def tokenize_html(url,k=0):
    html = request.urlopen(url).read().decode('utf8')
    
    rawtext = BeautifulSoup(html, "lxml").get_text()
    
    tokens = word_tokenize(rawtext)
    
    if k>0:
         return( tokens[:k] )
    else:
         return( tokens )
     


"""
Part-of-Speech Tagging for every word
"""
def universal_tagging(tokens):
    tokens_and_tags = nltk.pos_tag(tokens, tagset='universal')
    tags = list(tag[1] for tag in tokens_and_tags)
    return (tokens_and_tags, tags)



"""
Part-of-Speech Tagging for unique word
"""
def unique_tagging(tokens):
    unique_tokens = set(tokens)
    tokens_and_tags = nltk.pos_tag(unique_tokens, tagset='universal')
    tags = list(tag[1] for tag in tokens_and_tags)
    return (tokens_and_tags, tags)



"""
Test Codes
"""
url = "http://www.gutenberg.org/cache/epub/1661/pg1661.txt"
tokens = tokenize_html(url)
universal_tokens_and_tags,universal_tags = universal_tagging(tokens)
unique_tokens_and_tags,unique_tags = unique_tagging(tokens)

temp = list()
for component in universal_tokens_and_tags:
    if component[1] != ".":
        temp.append(component[1])
    else:
        if component[0] != ".":
            
    
