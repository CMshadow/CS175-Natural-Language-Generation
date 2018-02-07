# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import nltk, codecs
from nltk import word_tokenize
from urllib import request
from bs4 import BeautifulSoup




"""
Get raw text from a HTML
"""
def generate_html_rawtext(url):
    html = request.urlopen(url).read().decode('utf8')
    rawtext = BeautifulSoup(html, "lxml").get_text()
    return rawtext



"""
Get raw text from a local text file
"""
def generate_local_rawtext(path):
    with codecs.open(path, 'r', 'utf8') as myfile:
        rawtext=myfile.read()
    return rawtext




"""
Get all sentences from the raw text
"""
def generate_all_sentences(rawtext):
    segment = rawtext.splitlines()
    segment = list(filter(None, segment))
    
    all_sentences = []
    
    temp=[]
    for index, obj in enumerate(segment):
        tokens = tokenize(obj)
        braket_check = 0;
        for jndex, word in enumerate(tokens):
            if word == "(" or word == "[" or word == "{" or word == "<":
                braket_check += 1
                continue
            if word == ")" or word == "]" or word == "}" or word == ">":
                braket_check -= 1
                continue
            if word == "." or word == ";" or word == "?" or word == "!":
                if jndex == len(tokens)-1 or tokens[jndex+1] != "''":
                    
                    temp.append(word)
                    all_sentences.append(temp)
                    temp=[]
                    continue
                else:
                    temp.append(word)
                    continue
            if word == "''":
                if jndex == len(tokens)-1 or tokens[jndex-1] == "." or tokens[jndex-1] == "?" or tokens[jndex-1] == "!" or tokens[jndex-1] == ";":
                    temp.append(word)
                    all_sentences.append(temp) 
                    temp=[]
                    continue
                else:
                    temp.append(word)
                    continue
            if braket_check == 0:
                temp.append(word)
    return all_sentences





"""
Tokenize a raw text
"""
def tokenize(rawtext):    
    tokens = word_tokenize(rawtext)    
    return tokens 
     


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
Generate sentence structures
"""
def generate_sentence_structures(list_of_sentences, unique_tokens_and_tags):
    for sentence in list_of_sentences:
        for index, word in enumerate(sentence):
            for x in unique_tokens_and_tags:
                if x[0] == word:
                    sentence[index] = x[1]
                    break
    return list_of_sentences
                
                
                
"""
Test Codes
"""
path = "/Users/cmshadow/Desktop/pg1661.txt"

rawtext = generate_local_rawtext(path)

tokens = tokenize(rawtext)

all_sentences = generate_all_sentences(rawtext)

unique_tokens_and_tags,unique_tags = unique_tagging(tokens)

all_sentences = generate_sentence_structures(all_sentences, unique_tokens_and_tags)

print(all_sentences)
            
            
    
