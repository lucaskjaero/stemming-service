# Spanish word segmentation
import spacy
import es_core_news_sm

from Common import drop_punctuation_and_numbers

__author__ = 'Lucas Kjaero'

# Load the nlp model once
nlp = es_core_news_sm.load(disable=['parser', 'tagger', 'ner'])


def segment_spanish(input_text):
    """Returns a set of words in a given document."""
    processed_document = nlp(input_text)

    tokens = drop_punctuation_and_numbers([word for word in processed_document])

    unique_tokens = set(tokens)
    return list(unique_tokens)
