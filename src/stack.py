class Stack:
    def __init__(self):
        self.stack = []

    def push(self, ele):
        self.stack.append(ele)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[len(self.stack)-1]

    def isEmpty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    def __str__(self):
        return str(self.stack)