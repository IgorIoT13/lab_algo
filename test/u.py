import unittest

from model.clasick import Pinguin


class MyTestCase(unittest.TestCase):


    def testVersion(self):
        input_valuer = [
            ['Storage_1', 'Lviv'],
            ['Striy', 'Lviv'],
            ['Storage_2', 'Storage_1'],
            ['Kiyv', 'Lviv'],
            ['Ternopil', 'Harkiv'],
            ['Storage_3', 'Ternopil'],
            ['Ternopil', 'Lviv']
        ]

        inputP = Pinguin(input_valuer)
        test =inputP.all_storage_graph()
        result = test
        self.assertEqual(test, result)


    def test_not(self):
        input_valuer = [
            ['ternopil', 'Lviv'],
            ['Striy', 'Lviv'],
            ['Lviv', 'ternopil'],
            ['Kiyv', 'Lviv'],
            ['Ternopil', 'Harkiv'],
            ['ternopil', 'Ternopil'],
            ['Ternopil', 'Lviv']
        ]
        inputP = Pinguin(input_valuer)
        test = inputP.all_storage_graph()
        print(test)
        self.assertEqual(test, [])









if __name__ == '__main__':
    unittest.main()
