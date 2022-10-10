# Customized Empty Exception
class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass

# Stack
class ArrayStack:
    """LIFO Stack implementation using a Python list as underlying storage."""
    def __init__(self):
        """Create an empty stack."""
        self._data = [ ] # nonpublic list instance

    def __len__(self):
        """Return the number of elements in the stack."""
        return len(self._data)

    def is_empty(self):
        """Return True if the stack is empty."""
        return len(self._data) == 0

    def push(self, e):
        """Add element e to the top of the stack."""
        self._data.append(e) # new item stored at end of list

    def top(self):
        """Return (but do not remove) the element at the top of the stack.
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty( ):
            raise Empty('Stack is empty')
        return self._data[-1] # the last item in the list

    def pop(self):
        """Remove and return the element from the top of the stack (i.e., LIFO).
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty( ):
            raise Empty('Stack is empty')
        return self._data.pop( ) # remove last item from list

# Implementation
s = ArrayStack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
print(len(s))
print(s.pop()) # removes
print(s.top()) # does not remove
print(s.is_empty())

""" 
Operation Running Time
S.push(e) - O(1)
S.pop() - O(1)
S.top() - O(1)
S.is empty() - O(1)
len(S) - O(1)
"""