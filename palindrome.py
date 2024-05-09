# Name: Nicholas Vickery
# Date: 1/24/2024
# Project: Palindrome Stack and queue

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

def is_palindrome(s):
    stack = Stack()
    queue = Queue()

    for char in s.lower():
        if char.isalpha(): 
            stack.push(char)
            queue.enqueue(char)

    while not stack.is_empty():
        if stack.pop() != queue.dequeue():
            return False

    return True

# Test the function
test_string = "Madam, I'm Adam"
print(is_palindrome(test_string))

# Test the function with a palindrome
test_string_1 = "A man, a plan, a canal, Panama"
print(f"Is '{test_string_1}' a palindrome? {is_palindrome(test_string_1)}")

# Test the function with a non-palindrome
test_string_2 = "This is not a palindrome"
print(f"Is '{test_string_2}' a palindrome? {is_palindrome(test_string_2)}")