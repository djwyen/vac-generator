'''
to tackle the bigger problem of a general form vocab generator I'll first define a vocab generator for Atlantean and see if that provides any generalizable insights
'''
import random

add_syllable_chance = .4

class Phoneme:
    def __init__(self, features, representation, proportion):
        '''
        Represents a given Phoneme in the context of a certain phonotactic system
        '''
        self.features = set(features) # contains, as strings, features of this segment, eg 'dorsal' 'syllabic' 'velar' 'voiced'
        self.representation = representation # how should this be romanized?
        self.proportion = proportion # represents the proportion of the time this sound appears, relative to others in its category
    
    def __str__(self):
        return self.representation
    
    def __add__(self, other):
        return self.representation + str(other)
    
    def __radd__(self, other):
        return str(other) + self.representation

    def isF(self, feature):
        '''
        feature: a str of a given feature
        Returns True if this Phoneme has a given feature
        e.g. <g>.isF('voiced') = True
        <g>.isF('fricative') = False
        '''
        return feature in self.features


class Syllable:
    def __init__(self, initial=False, final=False):
        '''
        initial: True if this syllable is the first in its word
        final: True if this syllable is the last in its word
        In some languages word boundaries can license different segments (eg initial clusters)
        Note that a syllable can be both initial and final if it is in a monosyllabic word.
        '''
        self.initial = initial
        self.final = final
        self.onset = []
        self.nucleus = []
        self.coda = []
    
    def getRime(self):
        return self.nucleus + self.coda


class Word:
    def __init__(self, pos, n_syllables):
        self.pos = pos
        self.n_syllables = n_syllables
        self.syllables = []
        

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

def generate_word(syllab_structure):
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

if __name__ == "__main__":
    initials = set()
    nuclei = set()
    codae = set()

    alveolars = ['t', 'tj', 'ts', 'tθ', 'tʃ', 'tɬ', 's', 'θ', 'ʃ', 'ɬ', 'n', 'l']
    velars = ['k', 'kl', 'kj', 'ks', 'kx', 'kʃ', 'kç', 'x', 'xn', 'xl', 'ç', 'çj', 'ŋ', 'j']
    vowels = ['a', 'i', 'u', 'a:', 'i:', 'u:']

    # maybe to prevent problems you should create a dictionary mapping the romanized strings to the Phoneme objects to prevent accidental variable name collisions?
    t = Phoneme({'consonant', 'alveolar', 'stop'}, 't', 1)
    tj = Phoneme({'consonant', 'alveolar', 'stop', 'palatalized'}, 'tj', 1)
    ts = Phoneme({'consonant', 'alveolar', 'affricate'}, 'ts', 1)
    tth = Phoneme({'consonant', 'alveolar', 'affricate'}, 'tθ', 1)
    ch = Phoneme({'consonant', 'alveolar', 'affricate'}, 'tʃ', 1)
    tll = Phoneme({'consonant', 'alveolar', 'affricate'}, 'tɬ', 1)
    s = Phoneme({'consonant', 'alveolar', 'fricative', 'sibilant'}, 's', 1)
    th = Phoneme({'consonant', 'alveolar', 'fricative'}, 'θ', 1)
    sh = Phoneme({'consonant', 'alveolar', 'fricative', 'sibilant'}, 'ʃ', 1)
    ll = Phoneme({'consonant', 'alveolar', 'fricative'}, 'ɬ', 1)
    n = Phoneme({'consonant', 'alveolar', 'sonorant', 'stop', 'nasal', 'voiced'}, 'n', 1)
    l = Phoneme({'consonant', 'alveolar', 'sonorant', 'liquid', 'approximant', 'voiced'}, 'l', 1)

    k = Phoneme({'consonant', 'velar', 'stop'}, 'k', 1)
    kl = Phoneme({'consonant',  'velar', 'stop', 'complex'}, 'kl', 1)
    kj = Phoneme({'consonant', 'velar', 'stop', 'palatalized'}, 'kj', 1)
    kx = Phoneme({'consonant'})



    # probably the faster way to do this is to compile a masterlist of phonemes, create separate lists for each attribute, then just iterate over each characteristic and check set membership