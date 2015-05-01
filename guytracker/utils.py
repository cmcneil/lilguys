from django.core.serializers.json import Serializer as JSONSerializer
import json
import pickle
import pycurl
from StringIO import StringIO
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

class CleanSerializer(JSONSerializer):
    """Allows user to exclude any number of named fields."""
    def __init__(self, *args, **kwargs):
        self.excludes = kwargs.pop('excludes', [])
        super(CleanSerializer, self).__init__()
    
    def end_object(self, obj):
        data = self._current
        for field in self.excludes:
            data.pop(field, None)
        self.objects.append(data)

def lilguys_to_JS(lilguys):
    serializer = CleanSerializer(excludes = ['code', 'timestamp'])
    return serializer.serialize(lilguys)


def coords_to_location_name(lat, lon):
    """coords is a list of (longitude, latitude, guy) tuples. 
       returns dictionary of location names of the city, state, and country"""

    url = 'https://maps.googleapis.com/maps/api/geocode/json?latlng=' + str(lat) + ',' + str(lon) +'&sensor=true'
    data = StringIO()

    c = pycurl.Curl()
#   c.setopt(c.WRITEDATA, data)
    c.setopt(c.WRITEFUNCTION, data.write) # leviathan is using an older version of pycurl:
    c.setopt(c.URL, url)
    c.perform()

    data_clean = data.getvalue().replace('\n', '')
    info = json.loads(data_clean)
    area_info = info['results'][0]["address_components"]

    return {"city": area_info[3]["long_name"],
            "state": area_info[5]["long_name"],
            "country": area_info[6]["long_name"],}
