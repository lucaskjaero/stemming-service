import re

__author__ = 'Lucas Kjaero'

PUNCTUATION_CHARACTERS = ",.?;'[]()（）`~!@#$%^&*/+_-=<>{}:，。？！·；：‘“、\"”《》"
number_pattern = re.compile("[0-9]+(.)*[0-9]*")

def drop_punctuation_and_numbers(iterable_text):
    """A generator that returns tokens in a text if they are not punctuation or numbers. Input must be iterable"""
    for token in iterable_text:
        token_string = str(token)
        if token_string not in PUNCTUATION_CHARACTERS and number_pattern.match(token_string) is None:
            yield token_string
