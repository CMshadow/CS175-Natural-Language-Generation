#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 16:59:47 2018

@author: cmshadow
"""

import gensim, random
import ngram_sentence as ns
from gensim.models import KeyedVectors



#def word2vec_generator(num_words, seed_word, bigram_words, sentence_structures, word_pos_map, pos_word_map, glove_file_path):
#    
#    gensim.scripts.glove2word2vec.glove2word2vec(glove_file_path, "word2vec.txt")
#
#    word_vectors = KeyedVectors.load_word2vec_format('word2vec.txt', binary=False)
#    
#    
#    
#    keys = bigram_words.keys()
#    for key in keys:
#        if len(key) != 1:
#            return "ERROR - bigram_words key size must be equal to 1"
#    
#    if num_words not in sentence_structures:
#        return "ERROR - num_words length does not match any key found in \
#               sentence_structures."
#    
#    initial_key = tuple([seed_word])
#    if initial_key not in bigram_words:
#        return "ERROR - seed_word is not a key in bigram_words"
#    
#    matching_structures = []
#    seed_pos = random.sample(word_pos_map[seed_word], 1)
#    for structure in sentence_structures[num_words]:
#        if structure[0] == seed_pos[0]:
#            matching_structures.append(structure)
#    if len(matching_structures) == 0:
#        return "ERROR - no sentences of length" + str(num_words) + "begins with" + seed_pos[0]
#    target_structure = random.sample(matching_structures, 1)
#    
#    s = ""
#    s += seed_word
#    previous_word = seed_word
#
#    NN_check = ""
#    NNS_check = ""
#    VB_check = ""
#    VBP_check = ""
#    VBZ_check = ""
#    VBN_check = ""
#    VBG_check = ""
#    VBD_check = ""
#    
#    if word_pos_map[seed_word] == 'NN':
#        NN_check = seed_word
#    elif word_pos_map[seed_word] == 'NNS':
#        NNS_check = seed_word
#    elif word_pos_map[seed_word] == 'VB':
#        VB_check = seed_word
#    elif word_pos_map[seed_word] == 'VBP':
#        VBP_check = seed_word
#    elif word_pos_map[seed_word] == 'VBZ':
#        VBZ_check = seed_word
#    elif word_pos_map[seed_word] == 'VBN':
#        VBN_check = seed_word
#    elif word_pos_map[seed_word] == 'VBG':
#        VBG_check = seed_word
#    elif word_pos_map[seed_word] == 'VBD':
#        VBD_check = seed_word
#    
#    print(target_structure[0])
#    
#    for i, pos in enumerate(target_structure[0]):
#        if i != 0:
#            #prev = tuple([previous_word])
#            #elligible_words = bigram_words[prev][pos]
#            
#            if pos == "." or pos == "," or pos == "!" or pos == "``" or pos == "''" or pos == "?" or pos == ":" or pos == ";" or pos == "'":
#                s += pos
#                previous_word = pos
#                continue
#            
#            elif pos == 'NN':
#                if NN_check != "":
#                    similarity_check = []
#                    elligible_words = bigram_words[tuple([previous_word])][pos]
#                    if len(elligible_words) != 0:
#                        for word in elligible_words:
#                            similarity_check.append(word_vectors.similarity(NN_check, word))
#                        index = similarity_check.index(max(similarity_check))
#                        s += " " + elligible_words[index]
#                        NN_check = elligible_words[index]
#                        previous_word = elligible_words[index]
#                    else:
#                        previous_word = word_vectors.most_similar(positive=[NN_check], topn=1)[0][0]
#                        s += " " + previous_word
#                        NN_check = previous_word
#                else:
#                    elligible_words = bigram_words[tuple([previous_word])][pos]
#                    if len(elligible_words) == 0:
#                        substitute = random.sample(pos_word_map[pos], 1)[0]
#                        previous_word = substitute
#                        s += " " + substitute
#                    else:
#                        previous_word = random.sample(elligible_words, 1)[0]
#                        s += " " + previous_word
#                        VBD_check = previous_word
#                    
#            elif pos == 'NNS':
#                if NNS_check != "":
#                    similarity_check = []
#                    elligible_words = bigram_words[tuple([previous_word])][pos]
#                    if len(elligible_words) != 0:
#                        for word in elligible_words:
#                            similarity_check.append(word_vectors.similarity(NNS_check, word))
#                        index = similarity_check.index(max(similarity_check))
#                        s += " " + elligible_words[index]
#                        NNS_check = elligible_words[index]
#                        previous_word = elligible_words[index]
#                    else:
#                        previous_word = word_vectors.most_similar(positive=[NNS_check], topn=1)[0][0]
#                        s += " " + previous_word
#                        NNS_check = previous_word
#                else:
#                    elligible_words = bigram_words[tuple([previous_word])][pos]
#                    if len(elligible_words) == 0:
#                        substitute = random.sample(pos_word_map[pos], 1)[0]
#                        previous_word = substitute
#                        s += " " + substitute
#                    else:
#                        previous_word = random.sample(elligible_words, 1)[0]
#                        s += " " + previous_word
#                        VBD_check = previous_word
#                    
#            elif pos == 'VB':
#                if VB_check != "":
#                    similarity_check = []
#                    elligible_words = bigram_words[tuple([previous_word])][pos]
#                    if len(elligible_words) != 0:
#                        for word in elligible_words:
#                            similarity_check.append(word_vectors.similarity(VB_check, word))
#                        index = similarity_check.index(max(similarity_check))
#                        s += " " + elligible_words[index]
#                        VB_check = elligible_words[index]
#                        previous_word = elligible_words[index]
#                    else:
#                        previous_word = word_vectors.most_similar(positive=[VB_check], topn=1)[0][0]
#                        s += " " + previous_word
#                        VB_check = previous_word
#                else:
#                    elligible_words = bigram_words[tuple([previous_word])][pos]
#                    if len(elligible_words) == 0:
#                        substitute = random.sample(pos_word_map[pos], 1)[0]
#                        previous_word = substitute
#                        s += " " + substitute
#                    else:
#                        previous_word = random.sample(elligible_words, 1)[0]
#                        s += " " + previous_word
#                        VBD_check = previous_word
#                    
#            elif pos == 'VBP':
#                if VBP_check != "":
#                    similarity_check = []
#                    elligible_words = bigram_words[tuple([previous_word])][pos]
#                    if len(elligible_words) != 0:
#                        for word in elligible_words:
#                            similarity_check.append(word_vectors.similarity(VBP_check, word))
#                        index = similarity_check.index(max(similarity_check))
#                        s += " " + elligible_words[index]
#                        VBP_check = elligible_words[index]
#                        previous_word = elligible_words[index]
#                    else:
#                        previous_word = word_vectors.most_similar(positive=[VBP_check], topn=1)[0][0]
#                        s += " " + previous_word
#                        VBP_check = previous_word
#                else:
#                    elligible_words = bigram_words[tuple([previous_word])][pos]
#                    if len(elligible_words) == 0:
#                        substitute = random.sample(pos_word_map[pos], 1)[0]
#                        previous_word = substitute
#                        s += " " + substitute
#                    else:
#                        previous_word = random.sample(elligible_words, 1)[0]
#                        s += " " + previous_word
#                        VBD_check = previous_word
#                    
#            elif pos == 'VBZ':
#                if VBZ_check != "":
#                    similarity_check = []
#                    elligible_words = bigram_words[tuple([previous_word])][pos]
#                    if len(elligible_words) != 0:
#                        for word in elligible_words:
#                            similarity_check.append(word_vectors.similarity(VBZ_check, word))
#                        index = similarity_check.index(max(similarity_check))
#                        s += " " + elligible_words[index]
#                        VBZ_check = elligible_words[index]
#                        previous_word = elligible_words[index]
#                    else:
#                        previous_word = word_vectors.most_similar(positive=[VBZ_check], topn=1)[0][0]
#                        s += " " + previous_word
#                        VBZ_check = previous_word
#                else:
#                    elligible_words = bigram_words[tuple([previous_word])][pos]
#                    if len(elligible_words) == 0:
#                        substitute = random.sample(pos_word_map[pos], 1)[0]
#                        previous_word = substitute
#                        s += " " + substitute
#                    else:
#                        previous_word = random.sample(elligible_words, 1)[0]
#                        s += " " + previous_word
#                        VBD_check = previous_word
#                    
#            elif pos == 'VBN':
#                if VBN_check != "":
#                    similarity_check = []
#                    elligible_words = bigram_words[tuple([previous_word])][pos]
#                    if len(elligible_words) != 0:
#                        for word in elligible_words:
#                            similarity_check.append(word_vectors.similarity(VBN_check, word))
#                        index = similarity_check.index(max(similarity_check))
#                        s += " " + elligible_words[index]
#                        VBN_check = elligible_words[index]
#                        previous_word = elligible_words[index]
#                    else:
#                        previous_word = word_vectors.most_similar(positive=[VBN_check], topn=1)[0][0]
#                        s += " " + previous_word
#                        VBN_check = previous_word
#                else:
#                    elligible_words = bigram_words[tuple([previous_word])][pos]
#                    if len(elligible_words) == 0:
#                        substitute = random.sample(pos_word_map[pos], 1)[0]
#                        previous_word = substitute
#                        s += " " + substitute
#                    else:
#                        previous_word = random.sample(elligible_words, 1)[0]
#                        s += " " + previous_word
#                        VBD_check = previous_word
#                    
#            elif pos == 'VBG':
#                if VBG_check != "":
#                    similarity_check = []
#                    elligible_words = bigram_words[tuple([previous_word])][pos]
#                    if len(elligible_words) != 0:
#                        for word in elligible_words:
#                            similarity_check.append(word_vectors.similarity(VBG_check, word))
#                        index = similarity_check.index(max(similarity_check))
#                        s += " " + elligible_words[index]
#                        VBG_check = elligible_words[index]
#                        previous_word = elligible_words[index]
#                    else:
#                        previous_word = word_vectors.most_similar(positive=[VBG_check], topn=1)[0][0]
#                        s += " " + previous_word
#                        VBG_check = previous_word
#                else:
#                    elligible_words = bigram_words[tuple([previous_word])][pos]
#                    if len(elligible_words) == 0:
#                        substitute = random.sample(pos_word_map[pos], 1)[0]
#                        previous_word = substitute
#                        s += " " + substitute
#                    else:
#                        previous_word = random.sample(elligible_words, 1)[0]
#                        s += " " + previous_word
#                        VBD_check = previous_word
#                    
#            elif pos == 'VBD':
#                if VBD_check != "":
#                    similarity_check = []
#                    elligible_words = bigram_words[tuple([previous_word])][pos]
#                    if len(elligible_words) != 0:
#                        for word in elligible_words:
#                            similarity_check.append(word_vectors.similarity(VBD_check, word))
#                        index = similarity_check.index(max(similarity_check))
#                        s += " " + elligible_words[index]
#                        VBD_check = elligible_words[index]
#                        previous_word = elligible_words[index]
#                    else:
#                        previous_word = word_vectors.most_similar(positive=[VBD_check], topn=1)[0][0]
#                        s += " " + previous_word
#                        VBD_check = previous_word
#                else:
#                    elligible_words = bigram_words[tuple([previous_word])][pos]
#                    if len(elligible_words) == 0:
#                        substitute = random.sample(pos_word_map[pos], 1)[0]
#                        previous_word = substitute
#                        s += " " + substitute
#                    else:
#                        previous_word = random.sample(elligible_words, 1)[0]
#                        s += " " + previous_word
#                        VBD_check = previous_word
#                    
#            else:
#                elligible_words = bigram_words[tuple([previous_word])][pos]
#                if len(elligible_words) == 0:
#                    substitute = random.sample(pos_word_map[pos], 1)[0]
#                    previous_word = substitute
#                    s += " " + substitute
#                else:
#                    previous_word = random.sample(elligible_words, 1)[0]
#                    s += " " + previous_word
#                        
#    return s

def word2vec_generator(num_words, seed_words, word_table, grammar_table, word_pos_map, pos_word_map, glove_file_path):
    
    # load word vectors
    gensim.scripts.glove2word2vec.glove2word2vec(glove_file_path, "word2vec.txt")
    word_vectors = KeyedVectors.load_word2vec_format('word2vec.txt', binary=False)
    print(word_vectors, type(word_vectors))    
    
    for key in word_table:
        if len(key) != len(seed_words):
            return ["ERROR"]
    
    word_key = tuple(seed_words)
    s = []
    
    for word in seed_words:
        s.append(word)
    
    NOUN_check = ""
    VERB_check = ""
    
    for word in seed_words:
        if "NN" in word_pos_map[word] or "NNS" in word_pos_map[word]:
            NOUN_check = word
    for word in seed_words:
        if "VB" in word_pos_map[word] or "VBG" in word_pos_map[word] or "VBD" in word_pos_map[word] or "VBN" in word_pos_map[word] or "VBP" in word_pos_map[word] or "VBZ" in word_pos_map[word]:
            VERB_check = word
            
    ### start looking at next part of speech
    i=0
    while(True):
        pos_key = []
        while (tuple(pos_key) not in grammar_table):
            pos_key = []
            for j in range(len(word_key)):
                pos_key.append(random.sample(word_pos_map[word_key[j]], 1)[0])
            
        pos_key = tuple(pos_key)
        
        next_pos = random.sample(grammar_table[pos_key], 1)[0]
        
        if len(word_table[word_key][next_pos]) == 0:
            elligible_pos = []
            for pos in word_table[word_key]:
                if len(word_table[word_key][pos]) != 0:
                    elligible_pos.append(pos)
            next_pos = random.sample(elligible_pos, 1)[0]
        
        next_word = ""
        
        if next_pos == 'NN' or next_pos == 'NNS':
            if NOUN_check != "":
                similar_words = word_vectors.most_similar(positive=[NOUN_check], topn=50)
                similar_pure_words = [w[0] for w in similar_words]
                random.shuffle(similar_pure_words)
                
                for x in similar_pure_words:
                    if x in pos_word_map[next_pos]:
                        print('\t GOOD NN similarity generated')
                        print('\t', x)
                        print()
                        next_word = x
                        NOUN_check = x
                        potential_key = random.sample(word_table[word_key][next_pos], 1)[0]
                        break;
            if NOUN_check == "" or next_word == "":                
                if word_key in word_table and len(word_table[word_key][next_pos]) != 0:
                    print('\t GOOD NN word table random generated')
                    next_word = random.sample(word_table[word_key][next_pos], 1)[0]
                    NOUN_check = next_word
                    potential_key = next_word
                else:
                    print('\t BAD NN pos word map random generated')
                    next_word = random.sample(pos_word_map[next_pos], 1)[0]
                    NOUN_check = next_word
                    potential_key = next_word

            s.append(next_word)
#        elif next_pos == 'VB' or next_pos == 'VBD' or next_pos == 'VBG' or next_pos == 'VBN' or next_pos == 'VBP' or next_pos == 'VBZ':
#            if VERB_check != "":
#                similar_words = word_vectors.most_similar(positive=[VERB_check], topn=50)
#                similar_pure_words = [w[0] for w in similar_words]
#                random.shuffle(similar_pure_words)
#                
#                for x in similar_pure_words:
#                    if x in pos_word_map[next_pos]:
#                        print('\t GOOD VB similarity generated')
#                        print('\t', x)
#                        print()
#                        next_word = x
#                        VERB_check = x
#                        potential_key = random.sample(word_table[word_key][next_pos], 1)[0]
#                        break;
#            if VERB_check == "" or next_word == "":                
#                if word_key in word_table and len(word_table[word_key][next_pos]) != 0:
#                    print('\t GOOD VB word table random generated')
#                    next_word = random.sample(word_table[word_key][next_pos], 1)[0]
#                    VERB_check = next_word
#                    potential_key = next_word
#                else:
#                    print('\t BAD VB pos word map random generated')
#                    next_word = random.sample(pos_word_map[next_pos], 1)[0]
#                    VERB_check = next_word
#                    potential_key = next_word
#
#            s.append(next_word)
        else:

            if word_key in word_table and len(word_table[word_key][next_pos]) != 0:
                print('\t GOOD word table random generated')
                next_word = random.sample(word_table[word_key][next_pos], 1)[0]
                potential_key = next_word
            else:
                print('\t BAD pos word map random generated')
                next_word = random.sample(pos_word_map[next_pos], 1)[0]
                potential_key = next_word
            s.append(next_word)
           
            
        next_key = []
        for j, word in enumerate(word_key):
            if j != 0:
                next_key.append(word)
        next_key.append(potential_key)
        word_key = tuple(next_key)
                        
                
        if i > num_words:
            if key[-1] == "." or key[-1] == ";" or key[-1] == "?" or key[-1] == "!" or key[-1] == ":":
                return s
            for pos in word_table[key]:
                if (pos == "." or pos == ";" or pos == ":" or pos == "?" or pos == "!") and len(word_table[key][pos]) != 0:
                    s.append(random.sample(word_table[key][pos], 1)[0])
                    return s

        i += 1
        
    return s
    
    

#glove_file_path = "/Users/cmshadow/Desktop/glove.6B/glove.6B.50d.txt"
#
import glob
folder_path = "/Users/cmshadow/Documents/GitHub/CS175-Natural-Language-Generation/Speech"
file_names = glob.glob(folder_path + "/*.txt")
#print (file_names)
speeches = ns.generate_local_rawtext(file_names)
speech_tags, speech_tokens = ns.universal_tagging(ns.tokenize(speeches))

n_grams = 3
word_table, grammar_table, word_pos_map, pos_word_map = ns.build_ngram_tables(speech_tags, n_grams)
#sentence_structures = ns.from_path_to_sentence_structures(["obama_speeches.txt","./Speech/speech2.txt","./Speech/speech3.txt","./Speech/speech4.txt","./Speech/speech5.txt","./Speech/speech6.txt","./Speech/speech7.txt","./Speech/speech8.txt","./Speech/speech9.txt","./Speech/speech10.txt","./Speech/speech11.txt"], 'local')
#
#s = word2vec_generator(9, "I", ngram_table, sentence_structures, word_pos_map, pos_word_map, glove_file_path)
#print(s)


#summaries = ns.generate_booksummary_tokens(9999)

#n_grams = 3
#word_table, grammar_table, word_pos_map, pos_word_map = ns.build_ngram_tables(summaries, n_grams)
glove_file_path = "/Users/cmshadow/Desktop/glove.6B/glove.6B.50d.txt"

initializer = ["I", "am"]
#s = word2vec_generator(7, initializer, word_table, grammar_table, word_pos_map, pos_word_map, glove_file_path)
#print (s)

gensim.scripts.glove2word2vec.glove2word2vec(glove_file_path, "word2vec.txt")
word_vectors = KeyedVectors.load_word2vec_format('word2vec.txt', binary=False)

lengths = [ 8, 10, 16, 22 ]

initializer = ["I", "am"]
string = []
for i in range(15):
    num_words = random.sample(lengths,1)[0]
    s = word2vec_generator(num_words, initializer, word_table, grammar_table, word_pos_map, pos_word_map)
    string += s
    initializer = s[-(n_grams-1):]

