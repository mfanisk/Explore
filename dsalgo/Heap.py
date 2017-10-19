class BinaryMinHeap():
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def insert(self,value):
        self.heapList.append(value)
        self.currentSize = self.currentSize + 1
        self.perculateUp(self.currentSize)

    def perculateUp(self,i):
        while(i // 2 > 0):
            if(self.heapList[i//2] > self.heapList[i]):
                temp = self.heapList[i]
                self.heapList[i] = self.heapList[i//2]
                self.heapList[i//2] = temp
            i = i // 2

    def minChild(self,i):
        if 2 * i + 1 > self.currentSize:
            return 2 * i
        else:
            if(self.heapList[2 * i] < self.heapList[2 * i + 1]):
                return 2 * i
            else:
                return 2 * i + 1

    def perculateDown(self,i):
        while(i * 2 <= self.currentSize):
            minChildIndex = self.minChild(i)
            if(self.heapList[minChildIndex] < self.heapList[i]):
                temp = self.heapList[i]
                self.heapList[i] = self.heapList[minChildIndex]
                self.heapList[minChildIndex] = temp
            i = minChildIndex

