"""This module translates from French to English and back again"""
from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """Translation from English to French"""
    french_text = MyMemoryTranslator(source='en', target='fr').translate(english_text)
    return french_text

def french_to_english(french_text):
    """French to English translation"""
    english_text = MyMemoryTranslator(source='fr', target='en').translate(french_text)
    return english_text
