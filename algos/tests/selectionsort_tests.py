from unittest import TestCase
from random import random
from algos.selectionsort import selectionsort

class SelectionsSortTest(TestCase):
    def test_selection_sort(self):
        seq = [random() for _ in range(4000)]
        sorted_seq = sorted(seq)
        self.assertEqual(selectionsort(seq), sorted_seq)
    
    def test_selection_sort_2(self):
        self.assertEqual(selectionsort(list()), list())
    
if __name__ == '__main__':
    unittest.main()