#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 16:59:47 2018

@author: cmshadow
"""

import gensim, random
import ngram_sentence as ns
from gensim.models import KeyedVectors



def word2vec_generator(num_words, seed_word, bigram_words, sentence_structures, word_pos_map, pos_word_map, glove_file_path):
    
    gensim.scripts.glove2word2vec.glove2word2vec(glove_file_path, "word2vec.txt")

    word_vectors = KeyedVectors.load_word2vec_format('word2vec.txt', binary=False)
    
    
    
    keys = bigram_words.keys()
    for key in keys:
        if len(key) != 1:
            return "ERROR - bigram_words key size must be equal to 1"
    
    if num_words not in sentence_structures:
        return "ERROR - num_words length does not match any key found in \
               sentence_structures."
    
    initial_key = tuple([seed_word])
    if initial_key not in bigram_words:
        return "ERROR - seed_word is not a key in bigram_words"
    
    matching_structures = []
    seed_pos = random.sample(word_pos_map[seed_word], 1)
    for structure in sentence_structures[num_words]:
        if structure[0] == seed_pos[0]:
            matching_structures.append(structure)
    if len(matching_structures) == 0:
        return "ERROR - no sentences of length" + str(num_words) + "begins with" + seed_pos[0]
    target_structure = random.sample(matching_structures, 1)
    
    s = ""
    s += seed_word
    previous_word = seed_word

    NN_check = ""
    NNS_check = ""
    VB_check = ""
    VBP_check = ""
    VBZ_check = ""
    VBN_check = ""
    VBG_check = ""
    VBD_check = ""
    
    if word_pos_map[seed_word] == 'NN':
        NN_check = seed_word
    elif word_pos_map[seed_word] == 'NNS':
        NNS_check = seed_word
    elif word_pos_map[seed_word] == 'VB':
        VB_check = seed_word
    elif word_pos_map[seed_word] == 'VBP':
        VBP_check = seed_word
    elif word_pos_map[seed_word] == 'VBZ':
        VBZ_check = seed_word
    elif word_pos_map[seed_word] == 'VBN':
        VBN_check = seed_word
    elif word_pos_map[seed_word] == 'VBG':
        VBG_check = seed_word
    elif word_pos_map[seed_word] == 'VBD':
        VBD_check = seed_word
    
    print(target_structure[0])
    
    for i, pos in enumerate(target_structure[0]):
        if i != 0:
            #prev = tuple([previous_word])
            #elligible_words = bigram_words[prev][pos]
            
            if pos == "." or pos == "," or pos == "!" or pos == "``" or pos == "''" or pos == "?" or pos == ":" or pos == ";" or pos == "'":
                s += pos
                previous_word = pos
                continue
            
            elif pos == 'NN':
                if NN_check != "":
                    similarity_check = []
                    elligible_words = bigram_words[tuple([previous_word])][pos]
                    if len(elligible_words) != 0:
                        for word in elligible_words:
                            similarity_check.append(word_vectors.similarity(NN_check, word))
                        index = similarity_check.index(max(similarity_check))
                        s += " " + elligible_words[index]
                        NN_check = elligible_words[index]
                        previous_word = elligible_words[index]
                    else:
                        previous_word = word_vectors.most_similar(positive=[NN_check], topn=1)[0][0]
                        s += " " + previous_word
                        NN_check = previous_word
                else:
                    elligible_words = bigram_words[tuple([previous_word])][pos]
                    if len(elligible_words) == 0:
                        substitute = random.sample(pos_word_map[pos], 1)[0]
                        previous_word = substitute
                        s += " " + substitute
                    else:
                        previous_word = random.sample(elligible_words, 1)[0]
                        s += " " + previous_word
                        VBD_check = previous_word
                    
            elif pos == 'NNS':
                if NNS_check != "":
                    similarity_check = []
                    elligible_words = bigram_words[tuple([previous_word])][pos]
                    if len(elligible_words) != 0:
                        for word in elligible_words:
                            similarity_check.append(word_vectors.similarity(NNS_check, word))
                        index = similarity_check.index(max(similarity_check))
                        s += " " + elligible_words[index]
                        NNS_check = elligible_words[index]
                        previous_word = elligible_words[index]
                    else:
                        previous_word = word_vectors.most_similar(positive=[NNS_check], topn=1)[0][0]
                        s += " " + previous_word
                        NNS_check = previous_word
                else:
                    elligible_words = bigram_words[tuple([previous_word])][pos]
                    if len(elligible_words) == 0:
                        substitute = random.sample(pos_word_map[pos], 1)[0]
                        previous_word = substitute
                        s += " " + substitute
                    else:
                        previous_word = random.sample(elligible_words, 1)[0]
                        s += " " + previous_word
                        VBD_check = previous_word
                    
            elif pos == 'VB':
                if VB_check != "":
                    similarity_check = []
                    elligible_words = bigram_words[tuple([previous_word])][pos]
                    if len(elligible_words) != 0:
                        for word in elligible_words:
                            similarity_check.append(word_vectors.similarity(VB_check, word))
                        index = similarity_check.index(max(similarity_check))
                        s += " " + elligible_words[index]
                        VB_check = elligible_words[index]
                        previous_word = elligible_words[index]
                    else:
                        previous_word = word_vectors.most_similar(positive=[VB_check], topn=1)[0][0]
                        s += " " + previous_word
                        VB_check = previous_word
                else:
                    elligible_words = bigram_words[tuple([previous_word])][pos]
                    if len(elligible_words) == 0:
                        substitute = random.sample(pos_word_map[pos], 1)[0]
                        previous_word = substitute
                        s += " " + substitute
                    else:
                        previous_word = random.sample(elligible_words, 1)[0]
                        s += " " + previous_word
                        VBD_check = previous_word
                    
            elif pos == 'VBP':
                if VBP_check != "":
                    similarity_check = []
                    elligible_words = bigram_words[tuple([previous_word])][pos]
                    if len(elligible_words) != 0:
                        for word in elligible_words:
                            similarity_check.append(word_vectors.similarity(VBP_check, word))
                        index = similarity_check.index(max(similarity_check))
                        s += " " + elligible_words[index]
                        VBP_check = elligible_words[index]
                        previous_word = elligible_words[index]
                    else:
                        previous_word = word_vectors.most_similar(positive=[VBP_check], topn=1)[0][0]
                        s += " " + previous_word
                        VBP_check = previous_word
                else:
                    elligible_words = bigram_words[tuple([previous_word])][pos]
                    if len(elligible_words) == 0:
                        substitute = random.sample(pos_word_map[pos], 1)[0]
                        previous_word = substitute
                        s += " " + substitute
                    else:
                        previous_word = random.sample(elligible_words, 1)[0]
                        s += " " + previous_word
                        VBD_check = previous_word
                    
            elif pos == 'VBZ':
                if VBZ_check != "":
                    similarity_check = []
                    elligible_words = bigram_words[tuple([previous_word])][pos]
                    if len(elligible_words) != 0:
                        for word in elligible_words:
                            similarity_check.append(word_vectors.similarity(VBZ_check, word))
                        index = similarity_check.index(max(similarity_check))
                        s += " " + elligible_words[index]
                        VBZ_check = elligible_words[index]
                        previous_word = elligible_words[index]
                    else:
                        previous_word = word_vectors.most_similar(positive=[VBZ_check], topn=1)[0][0]
                        s += " " + previous_word
                        VBZ_check = previous_word
                else:
                    elligible_words = bigram_words[tuple([previous_word])][pos]
                    if len(elligible_words) == 0:
                        substitute = random.sample(pos_word_map[pos], 1)[0]
                        previous_word = substitute
                        s += " " + substitute
                    else:
                        previous_word = random.sample(elligible_words, 1)[0]
                        s += " " + previous_word
                        VBD_check = previous_word
                    
            elif pos == 'VBN':
                if VBN_check != "":
                    similarity_check = []
                    elligible_words = bigram_words[tuple([previous_word])][pos]
                    if len(elligible_words) != 0:
                        for word in elligible_words:
                            similarity_check.append(word_vectors.similarity(VBN_check, word))
                        index = similarity_check.index(max(similarity_check))
                        s += " " + elligible_words[index]
                        VBN_check = elligible_words[index]
                        previous_word = elligible_words[index]
                    else:
                        previous_word = word_vectors.most_similar(positive=[VBN_check], topn=1)[0][0]
                        s += " " + previous_word
                        VBN_check = previous_word
                else:
                    elligible_words = bigram_words[tuple([previous_word])][pos]
                    if len(elligible_words) == 0:
                        substitute = random.sample(pos_word_map[pos], 1)[0]
                        previous_word = substitute
                        s += " " + substitute
                    else:
                        previous_word = random.sample(elligible_words, 1)[0]
                        s += " " + previous_word
                        VBD_check = previous_word
                    
            elif pos == 'VBG':
                if VBG_check != "":
                    similarity_check = []
                    elligible_words = bigram_words[tuple([previous_word])][pos]
                    if len(elligible_words) != 0:
                        for word in elligible_words:
                            similarity_check.append(word_vectors.similarity(VBG_check, word))
                        index = similarity_check.index(max(similarity_check))
                        s += " " + elligible_words[index]
                        VBG_check = elligible_words[index]
                        previous_word = elligible_words[index]
                    else:
                        previous_word = word_vectors.most_similar(positive=[VBG_check], topn=1)[0][0]
                        s += " " + previous_word
                        VBG_check = previous_word
                else:
                    elligible_words = bigram_words[tuple([previous_word])][pos]
                    if len(elligible_words) == 0:
                        substitute = random.sample(pos_word_map[pos], 1)[0]
                        previous_word = substitute
                        s += " " + substitute
                    else:
                        previous_word = random.sample(elligible_words, 1)[0]
                        s += " " + previous_word
                        VBD_check = previous_word
                    
            elif pos == 'VBD':
                if VBD_check != "":
                    similarity_check = []
                    elligible_words = bigram_words[tuple([previous_word])][pos]
                    if len(elligible_words) != 0:
                        for word in elligible_words:
                            similarity_check.append(word_vectors.similarity(VBD_check, word))
                        index = similarity_check.index(max(similarity_check))
                        s += " " + elligible_words[index]
                        VBD_check = elligible_words[index]
                        previous_word = elligible_words[index]
                    else:
                        previous_word = word_vectors.most_similar(positive=[VBD_check], topn=1)[0][0]
                        s += " " + previous_word
                        VBD_check = previous_word
                else:
                    elligible_words = bigram_words[tuple([previous_word])][pos]
                    if len(elligible_words) == 0:
                        substitute = random.sample(pos_word_map[pos], 1)[0]
                        previous_word = substitute
                        s += " " + substitute
                    else:
                        previous_word = random.sample(elligible_words, 1)[0]
                        s += " " + previous_word
                        VBD_check = previous_word
                    
            else:
                elligible_words = bigram_words[tuple([previous_word])][pos]
                if len(elligible_words) == 0:
                    substitute = random.sample(pos_word_map[pos], 1)[0]
                    previous_word = substitute
                    s += " " + substitute
                else:
                    previous_word = random.sample(elligible_words, 1)[0]
                    s += " " + previous_word
                        
    return s

glove_file_path = "/Users/cmshadow/Desktop/glove.6B/glove.6B.50d.txt"

ngram_table, grammar_table, word_pos_map, pos_word_map = ns.from_path_to_ngram_tables(["obama_speeches.txt","./Speech/speech2.txt","./Speech/speech3.txt","./Speech/speech4.txt","./Speech/speech5.txt","./Speech/speech6.txt","./Speech/speech7.txt","./Speech/speech8.txt","./Speech/speech9.txt","./Speech/speech10.txt","./Speech/speech11.txt"], 'local', 2)
sentence_structures = ns.from_path_to_sentence_structures(["obama_speeches.txt","./Speech/speech2.txt","./Speech/speech3.txt","./Speech/speech4.txt","./Speech/speech5.txt","./Speech/speech6.txt","./Speech/speech7.txt","./Speech/speech8.txt","./Speech/speech9.txt","./Speech/speech10.txt","./Speech/speech11.txt"], 'local')

s = word2vec_generator(9, "I", ngram_table, sentence_structures, word_pos_map, pos_word_map, glove_file_path)
print(s)