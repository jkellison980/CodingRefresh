import unittest
import old.reference_functions as rf

class test_binary_search(unittest.TestCase):
    
    def test_found(self):
        arr = [1, 2, 3, 4, 5]
        target = 2
        self.assertEqual(rf.binary_search(arr, 2), 1, "\nFAIL: test_found for binary search\n")

    def test_not_found(self):
        arr = [1, 2, 3, 4, 5]
        target = 2
        self.assertEqual(rf.binary_search(arr, 9), -1, "\nFAIL: test_not_found for binary search\n")

class test_binary_sort(unittest.TestCase):

    def test_sort_basic(self):
        arr = [5, 1, 4, 2]
        self.assertEqual(rf.binary_sort(arr), [1, 2, 4, 5], "\nFAIL: test_sort_basic for binary sort")
    
    def test_sort_empty(self):
        arr = []
        self.assertEqual(rf.binary_sort(arr), [], "\nFAIL: test_sort_empty for binary sort")

    def test_single_array_obj(self):
        arr = [1]
        self.assertEqual(rf.binary_sort(arr), [1], "\nFAIL: test_single_array_obj for binary sort")

    def test_sort_long(self):
        arr = [48, 14, 61, 5, 34, 27, 21, 2, 70, 45, 24, 11, 66, 9, 57, 18, 38, 30, 41, 52]
        self.assertEqual(rf.binary_sort(arr),
                         [2, 5, 9, 11, 14, 18, 21, 24, 27, 30, 34, 38, 41, 45, 48, 52, 57, 61, 66, 70],
                         "\nFAIL: test_sort_long for binary sort")
        
class test_merge_sort(unittest.TestCase):

    def test_sort_basic(self):
        arr = [5, 1, 4, 2]
        self.assertEqual(rf.merge_sort(arr), [1, 2, 4, 5], "\nFAIL: test_sort_basic for merge sort")
    
    def test_sort_empty(self):
        arr = []
        self.assertEqual(rf.merge_sort(arr), [], "\nFAIL: test_sort_empty for merge sort")

    def test_single_array_obj(self):
        arr = [1]
        self.assertEqual(rf.merge_sort(arr), [1], "\nFAIL: test_single_array_obj for merge sort")

    def test_sort_long(self):
        arr = [48, 14, 61, 5, 34, 27, 21, 2, 70, 45, 24, 11, 66, 9, 57, 18, 38, 30, 41, 52]
        self.assertEqual(rf.merge_sort(arr),
                         [2, 5, 9, 11, 14, 18, 21, 24, 27, 30, 34, 38, 41, 45, 48, 52, 57, 61, 66, 70],
                         "\nFAIL: test_sort_long for merge sort")



if __name__ == "__main__":
    unittest.main()