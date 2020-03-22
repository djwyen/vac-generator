'''
to tackle the bigger problem of a general form vocab generator I'll first define a vocab generator for Atlantean and see if that provides any generalizable insights
'''
import random

add_syllable_chance = .4

def generate_syllable(stressed=False, initial=False, final=False):
    '''
    Return a phonotactically valid syllable, which may depend on our position in the word (whether we are at the start or end of the word, and whether this syllable is stressed)
    '''
    # in pseudocode:
    initial = generate_initial()
    nucleus = generate_nucleus()
    coda = generate_coda()
    rime = nucleus + coda
    syllable = initial + rime
    return syllable

def generate_word():
    word = ''
    # because the validity of a given segment in a syllable depends on whether this is the final syllable, counterintuitively, we must first decide whether or not to generate an additional syllable before deciding the contents of the current syllable
    final_syllable = False
    if random.random() > add_syllable_chance:
        final_syllable = True
    word += generate_syllable(final=final_syllable)
    

def generate_vocab(n, k=None):
    '''
    Return n words. One can also specify a word length k (in syllables).
    '''
    vocab = []
    for _ in range(n):
        vocab.append(generate_word())
    return vocab