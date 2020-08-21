# Originally proposed inventory:
# C = ['t', 'tj', 'ts', 'tθ', 'tʃ', 'tɬ', 's', 'θ', 'ʃ', 'ɬ', 'n', 'l', 'k', 'kl', 'kj', 'ks', 'kx', 'kʃ', 'kç', 'x', 'xn', 'xl', 'ç', 'çj', 'ŋ', 'j']
# V = ['a', 'i', 'u', 'a:', 'i:', 'u:']

# I have decided to change up the inventory.
# reasoning: it's weird to have the vowels i and u but only the semivowel j. It makes sense to add w. Note that even languages without labials can have the labiovelar approximant 'w', such as Mohawk, Seneca, Wichita, and Tlingit. I also think two sibilants is unnecessary, no matter how fun 'kʃ' is.

# languages sounds are modeled off of:
# Ryukyuan languages (eg Miyako and Irabu)
# N. Athabaskan languages (eg Chipewyan)
# Nuxalk
# Nahuatl
# and very marginally, Nahuatl, Ancient Greek, Berber languages, and Chinese languages (for rime structure mostly)

# second version of inventory + syllable structure:
# C = set(['t', 'ts', 'tθ', 'tɬ', 's', 'θ', 'ɬ', 'n', 'l', 'k', 'kl', 'kj', 'ks', 'kx', 'kç', 'x', 'xn', 'xl', 'ç', 'çj', 'ŋ'])
# V = set(['a', 'i', 'u', 'aː', 'iː', 'uː'])
# R = set(['n', 'l', 'ŋ'])
# M = set(['j', 'w'])
# F = set(['s', 'θ', 'ɬ', 'x', 'ç'])
# Atlantean syllable structure
# V , F , CF , CV , CMV , CFR , CVR , CMVR, RCV
# or more succinctly, (C(M))V(R) , (C)F(R) , (C)R

# import random
# import csv
# import os
# from datetime import datetime # for uniquely naming output logs

# TODO(derek)
# - implement illicit sequences
# - implement weights for different segments (instead of equal probabilities for each atm)
# - implement a UR/SR distinction
# - implement segmental features
# - implement production rules
# - implement suprasegmentals (stress, tone, etc)
# - implement more complex rules for extra syllable add-on besides geometric distribution
# You will notice that many of the above features seem interrelated, so think carefully about what order to implement things in

# current version of inventory + syllable structure:
# C = ['t', 'k']

# V = ['a', 'i', 'u']

# R for "resonant", aka a sonorant. I exclude semivowel sonorants; they can't be nuclei in my system.
# R = ['n', 'l', 'ŋ']

# M for "medial", which precedes vowels
# M = ['j', 'w']

# S for "syllabic", although with the current version this set also behaves like the medials.
# S = ['n', 'l', 'ŋ', 's', 'ɬ', 'x']

# maps an illegal sequence to how it is realized
# illegal_seqeuences = {
#     '#tx': '#t',
#     '#st': '#zt',
#     '#ɬt': '#ɮt',
#     '#xt': '#ɣt',
#     '#θk': '#ðk',
#     '#sk': '#zk',
#     '#ɬk': '#ɮk',
#     '#xk': '#ɣk',
#     '#θk': '#ðk',
# }


# seg_dict = {'C': C, 'V': V, 'R': R, 'M': M, 'S': S}

# you could write a script that converts the parentheses-based form of syllable structures (eg (R)(C)(M)V)
# syllable_structures = [
#     'CV',
#     'CMV',
#     'V',
#     'MV',
#     'SCV',
#     'SCMV',
#     'S',
#     'CS',
#     'CSV'
# ]

class WordGenerator:

    def __init__(self, syl_structs, seg_dict, add_syl_chance=0.6, max_syl_len=4):
        '''
        A
        syl_structs: an iterable of strings of capital letters, each representing a valid syllable structure in this language
        seg_dict: a dictionary of str to str which maps capital letters representing a given set of segments to an actual set of strings
        '''
        self.syl_structs = syl_structs
        self.seg_dict = seg_dict
        self.add_syl_chance = add_syl_chance
        self.max_syl_len = max_syl_len

    def get_syllable(self):
        syllable = ''
        struct = random.choice(self.syl_structs)
        for spot in struct:
            # get the relevant set of segments
            legal_segments = self.seg_dict[spot]
            syllable += random.choice(legal_segments)
        return syllable

    def get_word(self):
        # TODO(derek): in the future it might make sense to have a separate class for syllable generation and for word generation, in case you want to have the option of generating words according to custom distributions but keep syllables in the same distribution. On the other hand the syllable and word generation processes are interrelated since the phonotactics can engage with the position of a syllable in a word
        word = ''

        word += '#' # start with the left syllable boundary

        word += self.get_syllable() # a word has at least one syllable in it
        ticker = 1
        while ticker < self.max_syl_len and random.random() <= self.add_syl_chance:
            word += self.get_syllable()
            ticker += 1

        return word + '#' # finish with the right syllable boundary

# atl_wg = WordGenerator(syllable_structures, seg_dict)

# now = datetime.now()
# filename = os.path.join('log', now.strftime("%Y-%m-%d %H:%M:%S") + '.csv')

# with open(filename, 'w') as f:
#     for i in range(50):
#         f.write(atl_wg.get_word() + '\n')