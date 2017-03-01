from unittest import TestCase
from random import random
from algos.quicksort import quicksort, partition

class QuickSortTest(TestCase):
    def test_quick_sort(self):
        seq = [random() for _ in range(4000)]
        sorted_seq = sorted(seq)
        quicksort(seq, 0, len(seq)-1)
        self.assertEqual(seq, sorted_seq)
    
    def test_quick_sort_2(self):
        self.assertEqual(quicksort(list(), 0, 0), None)
    
if __name__ == '__main__':
    unittest.main()