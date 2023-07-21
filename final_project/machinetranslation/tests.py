import unittest
from machinetranslation.translator import english_to_french, french_to_english

class TestFrtoEnMethod(unittest.TestCase):
    def test_translateBonjour(self):
        french_text = 'Bonjour'
        transatedText = french_to_english(french_text)
        self.assertEqual(transatedText, "Hello")

class TestEntoFrMethod(unittest.TestCase):
    def test_translateBonjour(self):
        english_text = 'Hello'
        transatedText = english_to_french(english_text)
        self.assertEqual(transatedText, "Bonjour") 

if __name__ == '__main__':
    unittest.main()