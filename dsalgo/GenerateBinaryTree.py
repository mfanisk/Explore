import Queue
from dsalgo.BinaryTree import node
import random

class GenerateTree():
    def __init__(self,values = None):
        self.root = None
        self.generate(values)

    def generate(self,values):
        nodeQueue = Queue.Queue()
        self.root = node(values.pop(0))
        nodeQueue.enqueue(self.root)
        while(len(values) > 0):
            currentNode = nodeQueue.dequeue()
            if len(values) > 0:
                currentNode.left = node(values.pop(0))
                nodeQueue.enqueue(currentNode.left)
            if len(values) > 0:
                currentNode.right = node(values.pop(0))
                nodeQueue.enqueue(currentNode.right)