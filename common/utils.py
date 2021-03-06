import math
import time

import hashlib
from django.utils.crypto import get_random_string


def cheap_hash(string, length=6):
    _digest = hashlib.sha256(string.encode('utf-8')).hexdigest()
    if length > len(_digest):
        rand_str = get_random_string(length=length - len(_digest))
        _digest = '{d}{r}'.format(d=_digest, r=rand_str)
    return _digest[:length]


def meaningful_shorten(string, length=4):
    _consonant = ''.join([l for l in string.lower() if l.isalpha() and l not in 'aeiou'])
    if length > len(_consonant):
        rand_str = get_random_string(length=length - len(_consonant))
        _consonant = '{c}{r}'.format(c=_consonant, r=rand_str)
    return _consonant[:length]


def make_meanigful_id(string, length=10, cast_uppercase=True):
    _short = meaningful_shorten(string, length=int(math.ceil(length * 0.4)))
    _hash = cheap_hash(string + str(time.time()), length=int(math.ceil(length * 0.6)))
    _id = '{s}{h}'.format(s=_short, h=_hash)[:length]
    return _id.upper() if cast_uppercase else _id
