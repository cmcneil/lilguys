# This file generates a perfect min hash table in a very straightforward(kinda hacky) way:
# The reason this can be done is our server only wants to map integers in a given range
# to integers in another range of the same size, so this can be accomplished simply
# by taking a range of integers and shuffling.
import argparse
import pickle
import random
import sys

sys.path.append("../littleguys")
from settings import SECRET_KEY

def generate_min_hash(n, filename):
    codomain = range(n)
    random.seed(SECRET_KEY)
    random.shuffle(codomain)
    pickle.dump(codomain, open(filename, "wb"))


parser = argparse.ArgumentParser(description="Generate a perfect min hash table.")
parser.add_argument('N', metavar='N', type=int,
                    help="The range that we are mapping to itself.")
parser.add_argument('--output', metavar='output', dest='output', 
                    help="The file to save the output in. (output is a list : [0,N-1]->[0,N-1])")
args = parser.parse_args()
generate_min_hash(args.N, args.output)


