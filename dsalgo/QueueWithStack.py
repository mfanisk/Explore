class stack:
    def __init__(self):
        self.data = []

    def push(self,value):
        self.data.insert(0,value)

    def __str__(self):
        return str(self.data)

    def pop(self):
        return self.data.pop(0)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, item):
        return self.data[item]

    def peek(self):
        return self.data[0]

class MyQueue(object):
    def __init__(self):
        self.first = stack()
        self.second = stack()

    def peek(self):
        if(len(self.second) == 0):
            while(len(self.first) > 0):
                self.second.push(self.first.pop())
        return self.second.peek()

    def pop(self):
        if(len(self.second) == 0):
            while(len(self.first) > 0):
                self.second.push(self.first.pop())
        self.second.pop()

    def put(self, value):
        self.first.push(value)

queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())

