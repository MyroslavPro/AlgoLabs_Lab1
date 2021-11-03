import unittest
from lab1_algo_quicksort import QuickSort


class TestingQuickSort(unittest.TestCase):
    # ascending order
    def test_sorting_asc(self):
        array = [7, 3, 1, 4, 2, 6, 5]
        order = "asc"
        class_test = QuickSort()
        self.assertEqual(class_test.quick_sort(array, 0, len(array)-1, order), [1, 2, 3, 4, 5, 6, 7])

    def test_sorting_asc_worst_case(self):
        array = [7, 6, 5, 4, 3, 2, 1]
        order = "asc"
        class_test = QuickSort()
        self.assertEqual(class_test.quick_sort(array, 0, len(array)-1, order), [1, 2, 3, 4, 5, 6, 7])

    # descending order
    def test_sorting_desc(self):
        array = [2, 5, 1, 3, 7, 6, 4]
        order = "desc"
        class_test = QuickSort()
        self.assertEqual(class_test.quick_sort(array, 0, len(array)-1, order), [7, 6, 5, 4, 3, 2, 1])

    def test_sorting_desc_worst_case(self):
        array = [1, 2, 3, 4, 5, 6, 7]
        order = "desc"
        class_test = QuickSort()
        self.assertEqual(class_test.quick_sort(array, 0, len(array)-1, order),  [7, 6, 5, 4, 3, 2, 1])

    def test_none(self):
        array = []
        order = "asc"
        class_test = QuickSort()
        self.assertEqual(class_test.quick_sort(array, 0, len(array)-1, order), None)
