from unittest import TestCase
from random import random
from algos.bubblesort import bubblesort

class BubbleSortTest(TestCase):
    def test_bubble_sort(self):
        seq = [random() for _ in range(4000)]
        sorted_seq = sorted(seq)
        self.assertEqual(bubblesort(seq), sorted_seq)
    
    def test_bubble_sort_2(self):
        self.assertEqual(bubblesort(list()), list())
    
if __name__ == '__main__':
    unittest.main()