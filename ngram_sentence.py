# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 19:46:05 2018

@author: Daniel Maher
"""

"""
N-gram Building

All algorithms for parsing text files, web pages, etc. and building n-gram tables will be located here

"""

from bs4 import BeautifulSoup
import nltk, codecs
from nltk import word_tokenize
from urllib import request

def strip_html_tokenize_and_postag(url):
    """
    Strips html tags from the input webpage url, then tokenizes the remaining
    raw text into a list of part-of-speech tagged tokens in order of occurrence
    --------------------------------------------------------------------
    Inputs:
        url <string> : the url address of the webpage to be stripped of html tags
    Outputs:
        tokens <list of strings> : tokens of the raw text data contained at the url
    """    
    # get html page text from <url>
    html = request.urlopen(url).read().decode('utf8')
    # parse the html for raw text using BeautifulSoup
    rawtext = BeautifulSoup(html, 'html.parser').get_text()
    tokens = word_tokenize(rawtext)
    tokens = nltk.pos_tag(word_tokenize(rawtext), 'universal')
    return tokens

def open_file_tokenize_and_postag(filename):
    file = open(filename)
    rawtext = file.read()
    tokens = nltk.pos_tag(word_tokenize(rawtext), 'universal')
    return tokens

def build_ngram_tables(tokens, n_grams=2):
    """
    Takes a list of part-of-speech tagged tokens and produces 2 di
    --------------------------------------------------------------------
    Inputs:
        tokens <list of tuples> : a list of pairs of strings of the form (token, part-of-speech),
                ordered by order of occurrence in a text corpus
        n_grams <integer> : an integer representing the ngram value used for this table
    Outputs:
        word_table : a dictionary of the form {<list<string>>:{<string>:<list<tuple(<string>,<int>)>>}}
                e.g. for n_grams = 3:
                {('firstword', 'secondword') : {'NOUN' : ['dog', 'cat', ...
                                                 'VERB' : ['ran', 'ate', ...
        pos_table : a dictionary of 
        
    """
    
    # get pos tags from tokens
    tags = nltk.FreqDist([tup[1] for tup in tokens])
    tags = [tup for tup in tags]
    
    word_table = {}
    grammar_table = {}
    value_base = {}
    
    # initialize parts-of-speech keys for table
    for i in tags:
        value_base[i] = []
    
    key_size = n_grams - 1
    stop_index = len(tokens) - key_size
    
    import copy
    from collections import defaultdict
    i = 0
    while i < stop_index:
        word_key = []
        grammar_key = []
        
        pos_keys = copy.deepcopy(value_base)
        
        
        for j in range(key_size):
            word_key.append(tokens[i+j][0])
            grammar_key.append(tokens[i+j][1])
            
        next_word = tokens[i + key_size]
        
        # skip words in parenthesis
        left_bracket_count = 0
        right_bracket_count = 0
        if next_word[0] == "(":
            first_bracket_index = i + key_size
            left_bracket_count += 1
            while left_bracket_count != right_bracket_count:
                if tokens[i][0] == "(" and i != first_bracket_index:
                    left_bracket_count += 1
                if tokens[i][0] == ")":
                    right_bracket_count += 1
                i += 1
            next_word = tokens[i]
        
        word_key = tuple(word_key)
        grammar_key = tuple(grammar_key)
        if word_key not in word_table:
            word_table[word_key] = pos_keys
        if grammar_key not in grammar_table:
            grammar_table[grammar_key] = defaultdict(float)
            
        word_table[word_key][next_word[1]].append(next_word[0])
        grammar_table[grammar_key][next_word[1]] += 1.0
        
        i += 1
    
    for pos in grammar_table:
        total = 0
        for key in grammar_table[pos]:
            total += grammar_table[pos][key]
        for key in grammar_table[pos]:
            grammar_table[pos][key] /= total
    
    return word_table, grammar_table

word_ngrams, grammar_ngrams = build_ngram_tables(pos_tokens)






"""
-----------------------sentence structures---------------------
"""







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
    
    sentence_structures = {}
    
    for sentence in list_of_sentences:
        for index, word in enumerate(sentence):
            for x in unique_tokens_and_tags:
                if x[0] == word:
                    sentence[index] = x[1]
                    break
    
    for sentence in list_of_sentences:
        if len(sentence) in sentence_structures:
            sentence_structures[len(sentence)].append(sentence)
        else:
            sentence_structures[len(sentence)] = list()
            sentence_structures[len(sentence)].append(sentence)
    return sentence_structures

"""
Generate sentence structures in one procedure
"""
def from_path_to_sentence_structures(path):
    rawtext = generate_local_rawtext(path)
    tokens = tokenize(rawtext)
    all_sentences = generate_all_sentences(rawtext)
    unique_tokens_and_tags,unique_tags = unique_tagging(tokens)
    sentence_structures = generate_sentence_structures(all_sentences, unique_tokens_and_tags)
    return sentence_structures