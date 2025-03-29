from collections import deque

class Stack:
    def __init__(self):
        self.stack = deque()  # Using deque to store elements

    def push(self, item):
        """Insert an element at the top of the stack"""
        self.stack.append(item)

    def pop(self):
        """Remove and return the top element of the stack"""
        if self.is_empty():
            return "Stack is empty"
        return self.stack.pop()

    def peek(self):
        """Return the top element without removing it"""
        if self.is_empty():
            return "Stack is empty"
        return self.stack[-1]

    def is_empty(self):
        """Check if the stack is empty"""
        return len(self.stack) == 0

    def size(self):
        """Return the size of the stack"""
        return len(self.stack)

# Example Usage
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print("Top element:", stack.peek())  # Output: 30
print("Popped element:", stack.pop())  # Output: 30
print("Stack size:", stack.size())  # Output: 2
