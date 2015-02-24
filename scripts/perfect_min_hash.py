# This file generates a perfect min hash table in a very straightforward(kinda hacky) way:
# The reason this can be done is our server only wants to map integers in a given range
# to integers in another range of the same size, so this can be accomplished simply
# by taking a range of integers and shuffling.
import argparse
import os
import pickle
import random
import sys

from littleguys.settings import SECRET_KEY
#from settings import SECRET_KEY

# Where server side hash seeds etc. are stored.
CRYPT_DATA_ROOT = '/srv/media/lilguys_crypt_data'
#CRYPT_DATA_ROOT = ''

LILGUY_CODE_PMH_FILE = 'pmh_code.p'
LILGUY_URL_PMH_FILE = 'pmh_url.p'

URL_PMH_PATH = os.path.join(CRYPT_DATA_ROOT, LILGUY_URL_PMH_FILE)
CODE_PMH_PATH = os.path.join(CRYPT_DATA_ROOT, LILGUY_CODE_PMH_FILE)

LILGUY_CODE_PMH_INV_FILE = 'pmh_code_inv.p'
LILGUY_URL_PMH_INV_FILE = 'pmh_url_inv.p'

URL_PMH_INV_PATH = os.path.join(CRYPT_DATA_ROOT, LILGUY_URL_PMH_INV_FILE)
CODE_PMH_INV_PATH = os.path.join(CRYPT_DATA_ROOT, LILGUY_CODE_PMH_INV_FILE)
N_CODOMAIN = 45000
#N_CODOMAIN = 10

def generate_min_hash(n, filename, inv_filename, id=''):
    codomain = range(n)
    random.seed(SECRET_KEY+id)
    random.shuffle(codomain)
    pickle.dump(codomain, open(filename, "wb"))
    inv_map = range(n)
    for i in xrange(n):
        inv_map[codomain[i]] = i
    pickle.dump(inv_map, open(inv_filename, "wb"))

generate_min_hash(N_CODOMAIN, CODE_PMH_PATH, CODE_PMH_INV_PATH, 'code')
generate_min_hash(N_CODOMAIN, URL_PMH_PATH, URL_PMH_INV_PATH, 'url')


