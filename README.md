# Vac-Generator

A simple set of scripts to generate words for a conlang, which I hope to sophisticate with repeated changes.

Usage: run `python simple_generator.py [config] [n_words]`, where `config` is a config file and `n_words` is the number of words to generate. The results will be stored, line-by-line, in a text file under log.

## Formatting config files
A config file should be a .csv file.
The first line of a config file should be a comma-separated list of valid syllabic structures.
Each successive line should be a comma-separated list representing a certain set of segments (eg vowels, consonants, sonorants). The first entry of the line is the name of that set, and each entry in that line thereafter is one of the segments in that set.
 