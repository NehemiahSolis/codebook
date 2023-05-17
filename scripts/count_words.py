import collections
import re

def count_words(text):
    # Split words on spaces.
    counts = collections.defaultdict(int)
    W = re.sub(r"\s+", " ", text.lower()).split(' ')
    for w in W:
        counts[w] += 1

    return counts

def count_words_in_file(in_file, out_file):
    with open(in_file, 'r') as f:
        counts = count_words(f.read())

    with open(out_file, 'w') as f:
        for k in counts.keys():
            f.write( k + ","+ str(counts[k]) + "\n")