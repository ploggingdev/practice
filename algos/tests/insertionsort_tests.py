from unittest import TestCase
from random import random
from algos.insertionsort import insertionsort

class InsertionsSortTest(TestCase):
    def test_insertion_sort(self):
        seq = [random() for _ in range(4000)]
        sorted_seq = sorted(seq)
        self.assertEqual(insertionsort(seq), sorted_seq)
    
    def test_insertion_sort_2(self):
        self.assertEqual(insertionsort(list()), list())
    
if __name__ == '__main__':
    unittest.main()