from django.core.serializers.json import Serializer
import pickle
import sys

import scripts.perfect_min_hash as pmh


### Activation and URL code encryption!

# We add this number to the hash to make sure that all codes are at least 3 characters
# (that aren't 0) because that's visually appealing. I know it's a bit odd.
# Aesthetic preference man...
LILGUY_CODE_OFFSET = 1400 # Warning: Changing this number will change all URLs. Don't do it.

URL_PMH = pickle.load(open(pmh.URL_PMH_PATH, "rb"))
CODE_PMH = pickle.load(open(pmh.CODE_PMH_PATH, "rb"))

URL_PMH_INV = pickle.load(open(pmh.URL_PMH_INV_PATH, "rb"))
CODE_PMH_INV = pickle.load(open(pmh.CODE_PMH_INV_PATH, "rb"))

def lilguy_id_to_urlsafe_code(id):
    """
    Takes the index of a lilguy(it's creation number), and turns it into a URL safe code.
    The code is a bijection. Effectively, it distributes the numbers over a space, and
    then translates to hexidecimal.
    """
    return base36encode(URL_PMH[id] + LILGUY_CODE_OFFSET)

def lilguy_id_to_activation_code(id):
    """
    Takes the index of a lilguy(it's creation number), and turns it into a URL safe code.
    The code is a bijection. Effectively, it distributes the numbers over a space, and
    then translates to hexidecimal.
    """
    return base36encode(CODE_PMH[id] + LILGUY_CODE_OFFSET)

def urlsafe_code_to_lilguy_id(code):
    return URL_PMH_INV[base36decode(code) - LILGUY_CODE_OFFSET]

def activation_code_to_lilguy_id(code):
    return CODE_PMH_INV[base36decode(code) - LILGUY_CODE_OFFSET]

def base36encode(number, alphabet='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    """
    Converts an integer to a base36 string.
    Source: http://en.wikipedia.org/wiki/Base_36#Python_implementation
    """
    if not isinstance(number, (int, long)):
        raise TypeError('number must be an integer')
    base36 = ''
    sign = ''
    
    if number < 0:
        sign = '-'
        number = -number
        
    if 0 <= number < len(alphabet):
        return sign + alphabet[number]
    
    while number != 0:
        number, i = divmod(number, len(alphabet))
        base36 = alphabet[i] + base36
        
    return sign + base36

def base36decode(number):
    """Converts a base36 string to an integer."""
    return int(number, 36)

### Django Model to JS object serialization

class CleanSerializer(Serializer):
    def __init__(self, *args, **kwargs):
        self.excludes = kwargs.pop('excludes', [])
        
    def get_dump_object(self, obj):
        print "dump CALLED! ************"
        dump_object = self._current or {}
        for field in self.excludes:
            if field in dump_object.keys():
                del dump_object[field]
        return dump_object

def lilguys_to_JS(lilguys):
    serializer = CleanSerializer(excudes=['code'])
    return serializer.serialize(lilguys)
