class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = collections.deque()
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.queue.appendleft(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.queue.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.queue[-1]
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.queue
