class stack:
    def __init__(self):
        self.data = []

    def push(self,value):
        self.data.insert(0,value)

    def __str__(self):
        return str(self.data)

    def pop(self):
        self.data.pop(0)

print('hi')
myStack = stack()
myStack.push(1)
myStack.push(2)
myStack.push(3)
print(myStack)
myStack.pop()
print(myStack)