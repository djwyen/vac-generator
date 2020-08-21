import argparse
import simple_Atlantean_generator as gen
import csv
from datetime import datetime
import os

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="generate Atlantean words")
    
    parser.add_argument('--config', type=str, nargs='+', help='config file to use for phonotactics (see README for formatting details)')
    parser.add_argument('--n_words', type=int, default=50, nargs='?', help='number of words to generate')

    args = parser.parse_args()

    with open(args.config[0]) as f:
        reader = csv.reader(f)
        syl_structs = [str(s) for s in next(reader)]
        seg_dict = {}
        for row in reader:
            set_name = str(row[0])
            seg_dict[set_name] = [str(s) for s in row[1:]]
    
    wg = gen.WordGenerator(syl_structs, seg_dict)

    now = datetime.now()
    if not os.path.exists('log'):
        os.mkdir('log') 
    filename = os.path.join('log', now.strftime("%Y-%m-%d %H:%M:%S") + '.csv')
    with open(filename, 'w') as f:
        for i in range(args.n_words):
            f.write(wg.get_word() + '\n')
    


