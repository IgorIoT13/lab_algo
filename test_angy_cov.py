import unittest
from Stila import stilla
from intoExep import ErrorWithInfo

class MyTestCase(unittest.TestCase):
    def test_min_val_in_arr(self):
        cov = stilla(3, 3, [-1, 2, 5, 7, 1])
        cur = cov.finaly_cal()
        self.assertRaises(ErrorWithInfo)

    def test_two_val_cov(self):
        cov = stilla(3, 2, [1, 2, 5, 7, 1])
        cur = cov.finaly_cal()
        self.assertRaises(ErrorWithInfo)


    def test_two_val_N(self):
        cov = stilla(2, 3, [1, 2, 5, 7, 1])
        cur = cov.finaly_cal()
        self.assertRaises(ErrorWithInfo)


    def test_two_val_slot(self):
        cov = stilla(3, 2, [7, 1])
        cur = cov.finaly_cal()
        self.assertRaises(ErrorWithInfo)

    def test_two_val_cov(self):
        cov = stilla(3, 2, [-1, 2, 5, 7, 1])
        cur = cov.finaly_cal()
        self.assertRaises(ErrorWithInfo)

    def test_active(self):
        cov = stilla(5, 3, [1, 4, 6, 3, 12, 15, 9, 22, 44, 69, 24])
        cur = cov.finaly_cal()
        self.assertEqual(cur, 25)



if __name__ == '__main__':
    unittest.main()
