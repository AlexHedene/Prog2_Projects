# https://docs.python.org/3/library/unittest.html
import unittest

from MA1 import *


class Test(unittest.TestCase):

    def test_count(self):
        ''' Reasonable tests
        1. search empty lists
        2. count first, last and interior elements
        3. search for a list
        4. check that sublists on several levels are searched
        5. search non existing elements
        6. check that the list searched is not destroyed
        '''

        print('\nTests count')
        lst = [2,[1,2,3], [1,2,[1,2,3],1,2,3],[1,2,3],1,4,2]
        self.assertEqual(count(2,[]), 0)  #search empty lists
        self.assertEqual(count(2, lst), 7) #count first, last and interior elements
        self.assertEqual(count([1,2,3], lst),3) #search for a list and check that sublists on several levels are searched
        self.assertEqual(count([3,2,1],lst), 0) # search non existing elements
        self.assertEqual(lst,[2,[1,2,3], [1,2,[1,2,3],1,2,3],[1,2,3],1,4,2])

if __name__ == "__main__":
    unittest.main()
