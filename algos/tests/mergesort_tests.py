from unittest import TestCase
from random import random
from algos.mergesort import merge, mergesort

class MergeSortTest(TestCase):
    def test_merge_sort(self):
        seq = [random() for _ in range(4000)]
        sorted_seq = sorted(seq)
        self.assertEqual(mergesort(seq), sorted_seq)
    
    def test_merge_sort_2(self):
        self.assertEqual(mergesort(list()), list())
    
if __name__ == '__main__':
    unittest.main()