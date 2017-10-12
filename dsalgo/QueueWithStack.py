class MyQueue(object):
    def __init__(self):
        None

    def peek(self):
        None

    def pop(self):
        None

    def put(self, value):
        None

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

