<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 12:58:21 2018

@author: Daniel Maher
"""

from ngram_sentence import *

def stuctured_text_generator(num_words, seed_word, bigram_words, sentence_structures):
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
    if len(keys[0]) != 1:
        print ("ERROR - bigram_words key size must be equal to 1")
        return
    if num_words not in sentence_structures:
        print ("ERROR - num_words length does not match any key found in \
               sentence_structures.")
        return
    initial_key = tuple([seed_word])
    if initial_key not in bigram_words:
        print ("ERROR - seed_word is not a key in bigram_words")
        return
    
    
    return

=======
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 12:58:54 2018

@author: cmshadow
"""

import ngram_sentence as ns
>>>>>>> 23807dc4100d289cf6f07253816933b57fcf3dc0
