class Empty(Exception):
    pass

class ArrayQueue:
    """FIFO queue implementation using a Python list as underlying storage."""
    DEFAULT_CAPACITY = 10 # moderate capacity for all new queues

    def __init__(self):
        """Create an empty queue."""
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size

    def is_empty(self):
        """Return True if the queue is empty."""
        return self._size == 0

    def first(self):
        """Return (but do not remove) the element at the front of the queue.
        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._front]

    def dequeue(self):
        """Remove and return the first element of the queue (i.e., FIFO).
            Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._data[self._front]
        self._data[self._front] = None # help garbage collection
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer

    def enqueue(self, e):
        """Add an element to the back of queue."""
        if self._size == len(self._data):
            self._resize(2 * len(self._data)) # double the array size
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def resize(self, cap): # we assume cap >= len(self)
        """Resize to a new list of capacity >= len(self)."""
        old = self._data # keep track of existing list
        self._data = [None] * cap # allocate list with new capacity
        walk = self._front
        for k in range(self._size): # only consider existing elements
            self._data[k] = old[walk] # intentionally shift indices
            walk = (1 + walk) % len(old) # use old size as modulus
        self._front = 0 # front has been realigned

q = ArrayQueue()
print(len(q))
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(len(q))
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(len(q))


"""For the stack ADT, we created a very simple adapter class that used a Python list
as the underlying storage. It may be very tempting to use a similar approach for
supporting the queue ADT. We could enqueue element e by calling append(e) to
add it to the end of the list. We could use the syntax pop(0), as opposed to pop( ),
to intentionally remove the first element from the list when dequeuing.
As easy as this would be to implement, it is tragically inefficient. As we discussed
in Section 5.4.1, when pop is called on a list with a non-default index, a
loop is executed to shift all elements beyond the specified index to the left, so as to
fill the hole in the sequence caused by the pop. Therefore, a call to pop(0) always
causes the worst-case behavior of Θ(n) time.
We can improve on the above strategy by avoiding the call to pop(0) entirely.
We can replace the dequeued entry in the array with a reference to None, andmaintain
an explicit variable f to store the index of the element that is currently at the
front of the queue. Such an algorithm for dequeue would run in O(1) time. After
several dequeue operations, this approach might lead to the configuration portrayed
in Figure 6.5."""

