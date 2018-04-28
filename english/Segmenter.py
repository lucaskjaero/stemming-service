import re

# English word segmentation
import spacy
import en_core_web_sm


__author__ = 'Lucas Kjaero'

number_pattern = re.compile("[0-9]+(.)*[0-9]*")

# Load the nlp model once
nlp = en_core_web_sm.load(disable=['parser', 'tagger', 'ner'])


def drop_punctuation_and_numbers(iterable_text):
    """A generator that returns tokens in a text if they are not punctuation or numbers. Input must be iterable"""
    for token in iterable_text:
        token_string = str(token)
        if token_string not in ",.?;'[]()（）`~!@#$%^&*/+_-=<>{}:，。？！·；：‘“、\"" and number_pattern.match(token_string) is None:
            yield token_string


def segment_english(input_text):
    """Returns a set of words in a given document."""
    processed_document = nlp(input_text)

    tokens = drop_punctuation_and_numbers([word for word in processed_document])

    unique_tokens = set(tokens)
    return list(unique_tokens)
