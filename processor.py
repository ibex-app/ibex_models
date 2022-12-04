from enum import Enum


class Processor(str, Enum):
    tf_idf = 'tf_idf'
    speech_to_text = 'speech_to_text'
    ner = 'ner'
    face_recognition = 'face_recognition'
    sentiment = 'sentiment'
    hate_speech = 'hate_speech'
    topic = 'topic'
    botscore = 'botscore'
    detect_search_terms = 'detect_search_terms'
    top_engagement = 'top_engagement'
    detect_language = 'detect_language'

