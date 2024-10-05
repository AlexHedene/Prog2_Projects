""" linked_list.py

Student:
Mail:
Reviewed by:
Date reviewed:
"""


class LinkedList:

    class Node:
        def __init__(self, data, succ):
            self.data = data
            self.succ = succ

    def __init__(self):
        self.first = None

    def __iter__(self):            # Discussed in the section on iterators and generators
        current = self.first
        while current:
            yield current.data
            current = current.succ

    def __in__(self, x):           # Discussed in the section on operator overloading
        for d in self:
            if d == x:
                return True
            elif x < d:
                return False
        return False

    def insert(self, x):
        if self.first is None or x <= self.first.data:
            self.first = self.Node(x, self.first)
        else:
            f = self.first
            while f.succ and x > f.succ.data:
                f = f.succ
            f.succ = self.Node(x, f.succ)

    def print(self):
        print('(', end='')
        f = self.first
        while f:
            print(f.data, end='')
            f = f.succ
            if f:
                print(', ', end='')
        print(')')

    # To be implemented

    def length(self):
        f = self.first
        result = 0
        while f is not None:
            result += 1
            f = f.succ
        return result
            

    def mean(self):               
        pass

    def remove_last(self):       #
        f = self.first
        if f is None:
            raise ValueError("Cant remove last element, List is empty")
        elif f.succ is None:
            result = f.data
            self.first = f.succ
        else:
            while f.succ.succ is not None:
                f = f.succ
            result = f.succ.data
            f.succ = None
        return result

    def remove(self, x):
        f = self.first
        
        if f is None:
            return False
        
        if f.data == x:
            self.first = f.succ
            return True
       
        while f:
            if f.succ and f.succ.data == x:
                f.succ = f.succ.succ
                return True
            f = f.succ
        return False

        
        


    def to_list(self):            

        def _to_list(f):
            if f:
                return [f.data] + _to_list(f.succ)
            else:
                return []
        
        return _to_list(self.first)
            
            
            
    def remove_all(self, x):      #

        def _remove_all(x, f):
            if not f:
                return 0
            if f.succ and f.succ.data == x:
                f.succ = f.succ.succ
                return 1 + _remove_all(x, f)
            else:
                return _remove_all(x, f.succ)
                
        if self.first and self.first.data == x: # Check if first argument is x, and remove if thats the case
            result = _remove_all(x, self.first) + 1
            self.first = self.first.succ
        else:
            result = _remove_all(x, self.first)
        
        return result


    def __str__(self):            #
        return f"({', '.join(str(node) for node in self)})"

    def copy2(self):               #
        result = LinkedList()
        for x in self:
            result.insert(x)
        return result
    ''' Complexity for this implementation: 
        it will always need to insert at the end, and iterate over each element for every element
        This means that it is of order n * n --> n^2
    '''

    def copy(self):
        # Should be more efficient
        result = LinkedList()
        def _insert(f):
            if f.succ:
                _insert(f.succ)
                result.insert(f.data)
            else:
                result.insert(f.data)
        
        if self.first:
            _insert(self.first)
        return result
                
    ''' Complexity for this implementation:
        Since i use the fact that the list is ordered, i make a recursice function which inserts in reverse order. 
        This means that the insert function always insert directly, which make the insert function of order O(1).
        The resulting complexity is therefore O(n) + O(1) = O(n) instead of O(n^2) like the iterative copy function.
    '''
import time
import math

def main():
    large_list1 = [i for i in range(450)]
    large_list2 = [i for i in range(900)]
    lst1 = LinkedList()
    lst2 = LinkedList()
    # lst2 = LinkedList()
    for x in large_list1:
        lst1.insert(x)
    for x in large_list2:
        lst2.insert(x)
    start1 = time.perf_counter()
    a = lst1.copy()
    end1 = time.perf_counter()
    start2 = time.perf_counter()
    a = lst2.copy()
    end2 = time.perf_counter()
    order = math.log2((end2-start2)/(end1-start1))
    print(order)
    
    # lst.print()
    # print(lst.remove(3))
    # print(lst.remove(3))
    # print(lst.remove(3))
    # lst.print()
    # try:
    #     print(lst2.remove(3))
    # except ValueError as ve:
    #     print(ve)


    # Test code:


if __name__ == '__main__':
    main()
