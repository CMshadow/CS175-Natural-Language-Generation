# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 14:34:39 2018

@author: Daniel Maher
"""

import ngram_sentence as ns
import gensim, random
from gensim.models import KeyedVectors
from gensim.models import Word2Vec
import nltk, codecs

def word2vec_gen(num_words, word_table, grammar_table, seed_words, subject, word_pos_map, pos_word_map, file_path):
    with codecs.open(file_path, 'r', 'utf8') as f:
        summaries = f.read()
   
    summaries = nltk.word_tokenize(summaries)
    summaries = [nltk.word_tokenize(s.lower().replace('\n',' ').replace('--',' ').strip('"')) for s in summaries]
    
    model = Word2Vec(tokens, size=30, window=7, min_count=1, workers=4, sorted_vocab=1)
    vectors = model.wv
    del model
    
    s = []
    for word in seed_words:
        s.append(word)
    
    key = tuple(seed_words)
    i = 0
    while (True):
        pos_key = []
        while (tuple(pos_key) not in grammar_table):
            pos_key = []
            for j in range(len(key)):
                pos_key.append(random.sample(word_pos_map[key[j]], 1)[0])
            
        pos_key = tuple(pos_key)
        
        next_pos = random.sample(grammar_table[pos_key], 1)[0]
        if len(word_table[key][next_pos]) == 0:
            elligible_pos = []
            for pos in word_table[key]:
                if len(word_table[key][pos]) != 0:
                    elligible_pos.append(pos)
            next_pos = random.sample(elligible_pos, 1)[0]
            
        next_word = random.sample(word_table[key][next_pos], 1)[0]
        
        s.append(next_word)
        next_key = []
        for j, word in enumerate(key):
            if j != 0:
                next_key.append(word)
        next_key.append(next_word)
        key = tuple(next_key)
        
        if i > num_words:
            if key[-1] == "." or key[-1] == ";" or key[-1] == "?" or key[-1] == "!" or key[-1] == ":":
                return s
            for pos in word_table[key]:
                if (pos == "." or pos == ";" or pos == ":" or pos == "?" or pos == "!") and len(word_table[key][pos]) != 0:
                    s.append(random.sample(word_table[key][pos], 1)[0])
                    similarities = vectors.most_similar(positive=subject, topn=30)
                    print (similarities)
                    return s
        if i == 40:
            break
        i += 1
    
    similarities = vectors.most_similar(positive=subject, topn=30)
    print (similarities)
    return s


s = ["when", "he"]
filepath = './sample_summary_text.txt'
tokens = ns.open_file_tokenize_and_postag([filepath])

n_grams = 3
word_table, grammar_table, word_pos_map, pos_word_map = ns.build_ngram_tables(tokens, n_grams)

sentence = word2vec_gen(11, word_table, grammar_table, s, ["family"], word_pos_map, pos_word_map, filepath)

string = ""
for word in sentence:
    string += word + " "

print (string)




