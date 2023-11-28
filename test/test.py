import unittest
from models.ToTrip import Converter


class MyTestCase(unittest.TestCase):
    def test(self):
        test_patterns = [
            "afafaf",
            "afafa",
            "afafZ",
            "af1111",
            "Test",
            "test",
            "lab-5",
            "lab_6",
            "end"
        ]

        test_model = Converter(test_patterns)
        self.assertIsNotNone(test_model)

    def test_finder(self):
        test_patterns = [
            "Test",
            "festAn"
        ]
        test_model = Converter(test_patterns)
        self.assertEqual(len(test_model.converter().urls), 2)

    def test_Lower_case(self):
        test_patterns = [
            "Test",
            "Test"
        ]
        test_model = Converter(test_patterns)
        test_val = test_model.converter()
        self.assertEqual(len(test_val.urls), 1)


    def test_prefix_finder(self):
        test_patterns = [
            "afafaf",
            "afafa",
            "afafZ",
            "af1111",
            "Test",
            "test",
            "lab-5",
            "lab_6",
            "end"
        ]
        test_model = Converter(test_patterns)
        test_val = test_model.converter()
        result = test_model.find_prefix(test_val, 'af')
        result_com = ['afafz', 'afafa', 'afafaf', 'af1111']

        for i in result:
            if i not in result_com:
                self.assertTrue(False)
        self.assertTrue(True)

    def test_search(self):
        test_patterns = [
            "afafaf",
            "afafa",
            "afafZ",
            "af1111",
            "Test",
            "test",
            "lab-5",
            "lab_6",
            "end"
        ]
        test_model = Converter(test_patterns)
        test_val = test_model.converter()

        self.assertTrue(test_model.find('afafaf'))

if __name__ == '__main__':
    unittest.main()
