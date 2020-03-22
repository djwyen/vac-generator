
class Phoneme:
    def __init__(self):
        '''
        Represents a given Phoneme in the context of a certain phonotactic system
        '''
        self.features = set() # contains, as strings, features of this segment, eg 'dorsal' 'syllabic' 'velar' 'voiced'
        self.probability = 0 # represents the proportion of the time this sound appears, relative to others in its category
        self.representation = '' # how should this be romanized?
    
    def __str__(self):
        return self.representation
    
    def __add__(self, other):
        return self.representation + str(other)
    
    def __radd__(self, other):
        return str(other) + self.representation

class PhonotacticSystem:
    def __init__(self, onsets, nuclei, codas, rimes):
        '''
        Represents a phonotactic system, where one specifies sets of viable Phoneme segments in a given position
        '''

class VocabGenerator:
    def __init__(self, phonotactic_system):
        '''
        Initialize a new VocabGenerator, which takes a PhonotacticSystem and uses it to implement the following functions:
        GenerateWord(n) — return n words of any length
        GenerateWord(n, s) — return n words of length s
        '''
        self.terminate_prob = .7 # when generating a word, how likely the word is to be deemed 'finished' and have syllables stop being appended
    
    def generate_word(self, n=1):
        vocab = []
        for _ in range(n):
            current_word = ''
            current_word += self.generate_syllable
            vocab.append(current_word)
        return vocab

        