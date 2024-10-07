""" bst.py

Student: Alexander Hedene
Mail: alexander.hedene.3178@student.uu.se
Reviewed by: David
Date reviewed: 2024-10-07
"""


from linked_list import LinkedList


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

    def __iter__(self):         # Dicussed in the text on generators
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

    def contains1(self, k): #
        n = self.root
        while n and n.key != k:
            if k < n.key:
                n = n.left
            else:
                n = n.right
        return n is not None
    
    def contains(self, k):
        
        def _contains(k, r):
            if r:
                if r.key == k:
                    return True
                elif k < r.key:
                    return _contains(k,r.left)
                else:
                    return _contains(k, r.right)
            else:
                return False
        
        return _contains(k, self.root)
            

    def size(self):
        return self._size(self.root)

    def _size(self, r):
        if r is None:
            return 0
        else:
            return 1 + self._size(r.left) + self._size(r.right)

#
#   Methods to be completed
#

    def height(self):                 #            
        
        def _height(r):
            if r:
                return 1 + max(_height(r.left), _height(r.right))
            else:
                return 0
        return _height(self.root)

    def remove(self, key): #
        self.root = self._remove(self.root, key)

    def _remove(self, r, k):                      #
        if r is None:
            return None
        elif k < r.key:
            r.left = self._remove(r.left, k)
            # r.left = left subtree with k removed
        elif k > r.key:
            r.right = self._remove(r.right, k)
            # r.right =  right subtree with k removed
        else:  # This is the key to be removed
            if r.left is None:     # Easy case
                return r.right
            elif r.right is None:  # Also easy case
                return r.left
            else:  # This is the tricky case.
                min_node = r.right
                while min_node.left.left:
                    min_node = min_node.left
                r.key = min_node.left.key
                min_node.left = None
                # Find the smallest key in the right subtree
                # Put that key in this node
                # Remove that key from the right subtree
        return r  # Remember this! It applies to some of the cases above

    def __str__(self):                #            
        return f"<{', '.join(str(node) for node in self)}>"

    def to_list(self):                      #      
        # The complexity is O(n) since it visits each element once, and append has complexity O(1) --> O(n) + O(1) = O(n)
        result = []
        def _to_list(r):
            if r:
                _to_list(r.left)
                result.append(r.key)  # Here the order can be changed to perorder/postorder also
                _to_list(r.right)
            else:
                return []
        _to_list(self.root)
        return result

    def to_LinkedList(self):
        # The complexity is O(n) from visiting every element. For the insert method this is normally O(n) too.
        # Since i choose to create the linked list in reverse, and start insrting numbers from the three from right to left
        # I will always insert the biggest number first, which makes the insert method a O(1) * n in complexity.
        # The resulting complexity is therefore O(n) + O(n) = O(n)
        result = LinkedList()
        
        def _to_LinkedList(r):
            if r:
                _to_LinkedList(r.right)
                result.insert(r.key)
                _to_LinkedList(r.left)
        _to_LinkedList(self.root)
        
        return result


def random_tree(n):                               # Useful
    pass


def main():
    t = BST()
    for x in [12, 5, 2, 8, 7, 23, 17, 13, 21, 36, 42, 14]: #[4, 1, 3, 6, 7, 1, 1, 5, 8]:
        t.insert(x)
    print(t)
    print(t.to_LinkedList())
    print('size  : ', t.size())
    print('height  : ', t.height())
    for k in [13, 21, 12, 7, 2, 17, 42, 43, 14]:
        print(f"contains({k}): {t.contains(k)}")


if __name__ == "__main__":
    main()


"""
What is the generator good for?
==============================

1. computing size? Yes - only need to know number of nodes
2. computing height? No - The concept of height is gone using the generator
3. contains? Yes - Iterate trough the nodes, could be better optimized though
4. insert? No - Need to find a specific node and choose how to treverse the tree
5. remove? No -||-

"""
