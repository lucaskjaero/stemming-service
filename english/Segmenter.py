# English word segmentation
import spacy
import en_core_web_sm

from Common import drop_punctuation_and_numbers

__author__ = 'Lucas Kjaero'

# Load the nlp model once
nlp = en_core_web_sm.load(disable=['parser', 'tagger', 'ner'])


def segment_english(input_text):
    """Returns a set of words in a given document."""
    processed_document = nlp(input_text)

    tokens = drop_punctuation_and_numbers([word for word in processed_document])

    unique_tokens = set(tokens)
    return list(unique_tokens)
