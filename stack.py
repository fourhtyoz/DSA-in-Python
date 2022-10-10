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

# Put in practice

"""
An HTML document should have matching tags. We give a
Python function that matches tags in a string representing an HTML document. We
make a left-to-right pass through the raw string, using index j to track our progress
and the find method of the str class to locate the < and > characters that define
the tags. Opening tags are pushed onto the stack, and matched against closing tags
as they are popped from the stack, just as we did when matching delimiters in Code
Fragment 6.4. By similar analysis, this algorithm runs in O(n) time, where n is the
number of characters in the raw HTML source.
"""

def is_matched_html(raw):
    """Return True if all HTML tags are properly match; False otherwise."""
    S = ArrayStack()
    j = raw.find('<') # find first ’<’ character (if any)
    while j != -1:
        k = raw.find('>', j+1) # find next ’>’ character
        if k == -1:
            return False # invalid tag
        tag = raw[j+1:k] # strip away < >
        if not tag.startswith('/'): # this is opening tag
            S.push(tag)
        else: # this is closing tag
            if S.is_empty():
                return False # nothing to match with
            if tag[1:] != S.pop():
                return False # mismatched delimiter
        j = raw.find('<', k+1) # find next ’<’ character (if any)
    return S.is_empty() # were all opening tags matched?

html = "<body><center><h1></h1></center><p></p><ol><li></li><li></li><li></li></ol></body>"
print(is_matched_html(html))

"""
Each opening symbol must match its corresponding closing symbol. For example, a
left bracket, “[,” must match a corresponding right bracket, “],” as in the expression
[(5+x)-(y+z)]
"""

def is_matched(expr):
    """Return True if all delimiters are properly match; False otherwise."""
    lefty = '({[' # opening delimiters
    righty = ')}]' # respective closing delims
    S = ArrayStack()
    for c in expr:
        if c in lefty:
            S.push(c) # push left delimiter on stack
        elif c in righty:
            if S.is_empty( ):
                return False # nothing to match with
            if righty.index(c) != lefty.index(S.pop()):
                return False # mismatched
    return S.is_empty()

expression = '[(5+x)-(y+z)]'
print(is_matched(expression))