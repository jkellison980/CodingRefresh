import unittest
import src.reference_functions as rf

class test_binary_search_sorted_array(unittest.TestCase):
    
    def test_found(self):
        arr = [1, 2, 3, 4, 5]
        target = 2
        self.assertEqual(rf.binary_search_sorted_array(arr, 2), 1, "\n\nFAIL: test_found")
        

#class test_second_function(TBD):
