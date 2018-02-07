# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 12:58:21 2018

@author: Daniel Maher
"""

import ngram_sentence as ns

def structured_text_generator(num_words, seed_word, bigram_words, sentence_structures, word_pos_map):
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
    
    

    return

word_table, grammar_table, word_pos_map = ns.from_path_to_ngram_tables("http://www.gutenberg.org/cache/epub/1661/pg1661.txt", 'url', 2)
sentence_structures = ns.from_path_to_sentence_structures("http://www.gutenberg.org/cache/epub/1661/pg1661.txt", 'url')

structured_text_generator(8, "Sherlock", word_table, sentence_structures, word_pos_map)
