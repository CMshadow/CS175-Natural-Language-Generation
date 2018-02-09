# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 12:58:21 2018

@author: Daniel Maher
"""

import ngram_sentence as ns
import random

def structured_text_generator(num_words, seed_word, bigram_words, sentence_structures, word_pos_map, pos_word_map):
    """
    Generates text of length <num_words>, with <seed_word> as the first word
    of the text. Text generator consults <sentence_structures> and <bigram_words>
    tables to predict next word in text.
    
    ------------------------------------------------------------
    Inputs:
        num_words : an integer representing the number of words to be generated
        seed_word : a string representing the first wor
    """
    keys = bigram_words.keys()
    for key in keys:
        if len(key) != 1:
            print ("ERROR - bigram_words key size must be equal to 1")
        break
    if num_words not in sentence_structures:
        print ("ERROR - num_words length does not match any key found in \
               sentence_structures.")
        return
    initial_key = tuple([seed_word])
    
    if initial_key not in bigram_words:
        print ("ERROR - seed_word is not a key in bigram_words")
        return
    
    
    
    matching_structures = []
    seed_pos = random.sample(word_pos_map[seed_word], 1)
    for structure in sentence_structures[num_words]:
        if structure[0] == seed_pos[0]:
            matching_structures.append(structure)
    if len(matching_structures) == 0:
        print ("ERROR - no sentences of length", num_words,"begins with",seed_pos)
        return
    target_structure = random.sample(matching_structures, 1)
    
    s = ""
    s += seed_word
    previous_word = seed_word
    
    print (target_structure)
    
    for i, pos in enumerate(target_structure[0]):
        if i != 0:
            prev = tuple([previous_word])
            if pos in pos_word_map.keys():
                s += pos
                previous_word = pos
                continue
            elligible_words = bigram_words[prev][pos]
            if len(elligible_words) == 0:
                substitute = random.sample(pos_word_map[pos], 1)[0]
                previous_word = substitute
                s += " " + substitute
            else:
                previous_word = random.sample(elligible_words, 1)[0]
                s += " " + previous_word
                
    
    return s

word_table, grammar_table, word_pos_map, pos_word_map = ns.from_path_to_ngram_tables(["sherlock.txt", "cities.txt", "frankenstein.txt"], 'local', 2)
sentence_structures = ns.from_path_to_sentence_structures(["sherlock.txt", "cities.txt", "frankenstein.txt"], 'local')

seed = ""
num_words = 5
while True:
    seed = input("Enter seed word: ")
    num_words = int(input("Enter number of words: "))
    print ("\n")
    if num_words == 0:
        break
    s = structured_text_generator(num_words, seed, word_table, sentence_structures, word_pos_map, pos_word_map)
    print (s)
