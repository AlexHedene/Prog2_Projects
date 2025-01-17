"""
Solutions to module VA bst

Student: Alexander Hedene
Mail: Alex.hedene@gmail.com
"""

import random
import math
import numpy as np
class BST:

    class Node:
        def __init__(self, key, left=None, right=None):
            self.key = key
            self.left = left
            self.right = right

        def __iter__(self):     # Discussed in the text on generators
            if self.left:
                yield from self.left
            yield self.key
            if self.right:
                yield from self.right

    def __init__(self, root=None):
        self.root = root

    def __iter__(self):         # Discussed in the text on generators
        if self.root:
            yield from self.root

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, r, key):
        if r is None:
            return self.Node(key)
        elif key < r.key:
            r.left = self._insert(r.left, key)
        elif key > r.key:
            r.right = self._insert(r.right, key)
        else:
            pass  # Already there
        return r

    def print(self):
        self._print(self.root)

    def _print(self, r):
        if r:
            self._print(r.left)
            print(r.key, end=' ')
            self._print(r.right)

    def height(self):                 #            
    
        def _height(r):
            if r:
                return 1 + max(_height(r.left), _height(r.right))
            else:
                return 0
        return _height(self.root)

    def contains(self, k):
        n = self.root
        while n and n.key != k:
            if k < n.key:
                n = n.left
            else:
                n = n.right
        return n is not None

    def size(self):
        return self._size(self.root)

    def _size(self, r):
        if r is None:
            return 0
        else:
            return 1 + self._size(r.left) + self._size(r.right)



    def ipl(self):    
        def _ipl(r, count):
            if not r:
                return 0
            else:
                return count + _ipl(r.left, count + 1) + _ipl(r.right, count + 1)
        return _ipl(self.root,1)

def random_tree(n):                               # Useful
    t = BST()
    for _ in range(n):
        t.insert(random.random())
    return t


def main():
    height_list = []
    ipl_list = []
    j = 20
    for k in range(1,8):
        print(k)
        ipl_list_k = []
        height_list_k = []
        for _ in range(j):
            n = 1000*2**k
            t = random_tree(n)
            height_list_k.append(t.height())
            ipl_list_k.append(t.ipl())
        height_list.append(sum(height_list_k)/j/math.log(n))
        ipl_list.append(sum(ipl_list_k)/j/n)
    slope,_ = np.polyfit(np.arange(1,k+1), np.array(ipl_list), 1)
    print("All values of IPL")
    print(ipl_list)
    print(f"Calculated slope: {round(slope,3)}, Theorethical value: 1.39")
    print()
    print("Each height devided by log(n). This should be constant if height follows O(log(n))")
    print(height_list)
    print("The hieght needs to find one node, which is O(log(n)). IPL needs to find the height for every node which is n*O(log(n)) = O(nlog(n))")


if __name__ == "__main__":
    main()


"""

Results for ipl of random trees
===============================
How well does that agree with the theory?
The theory says: ipl(n) =  c*n*log(n). Then ipl(n)/n = c*log(n). If i calculate ipl(n)/n for 2^k and 2^(k+1) and tkae the differense:
c*log(2^(k+1)) - c*log(2^k) = c(k+1) - ck = c:
I did this for several n: 1-9 20 times each and calculate the slope:
It agrees very well with theory. I found the value of c in c*n*log(n) to be c = 1.401, and theorethical value is 1.39.
If you run the code you will calculate this value, and plot all ipl.


What can you guess about the
height?
The hieght needs to find one node, which is O(log(n)). IPL needs to find the height for every node which is n*O(log(n)) = O(nlog(n))
If you run the code the values of the height/log(n) will be printed
"""
