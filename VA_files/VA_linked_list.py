"""
Solutions to module VA linked lists

Student:
Mail:
"""


class LinkedList:

    class Node:
        def __init__(self, data, succ):
            self.data = data
            self.succ = succ
            
    def __init__(self):
        self.first = None

    def __iter__(self):       # Discussed in the section on iterators and generators
        current = self.first
        while current:
            yield current.data
            current = current.succ

    def __in__(self, x):      # Discussed in the section on operator overloading
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

    def __str__(self):
        lst = [str(i) for i in self]
        return f"({', '.join(lst)})"

    def print(self):
        print('(', end='')
        f = self.first
        while f:
            print(f.data, end='')
            f = f.succ
            if f:
                print(', ', end='')
        print(')')


class Person:                
    def __init__(self, name, pnr):
        self.name = name
        self.pnr = pnr

    def __str__(self):
        return f"{self.name}:{self.pnr}"
    
    def __lt__(self, other):
        return self.name < other.name
        
    def __le__(self, other):
        return self.name <= other.name
    
    def __eq__(self, other):
        return self.name == other.name

def main():
    plst = LinkedList()
    p = Person('A',1)
    plst.insert(p)
    plst.print()
    p2 = Person('C',3)
    plst.insert(p2)
    print(plst)
    p1 = Person('B',2)
    
    plst.insert(p1)
    plst.print()


if __name__ == '__main__':
    main()
