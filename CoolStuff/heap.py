class binaryheap:
    class Node:
        def __init__(self, data, weight):
            self.data = data
            self.weight = weight
    def __init__(self, max = True):
        self.heap = []
        self.max = max

    def addHelp(self, aNode):
        self.heap.append(aNode)
        self.heapifyUp(len(self.heap)-1)

    def add(self, data, weight):
        node = self.Node(data, weight)
        self.addHelp(node)

    def pop(self):
        junkNode = self.Node(None, float("-inf")*(-1 if self.max else 1))
        self.heap.append(junkNode)
        self.swap(0, len(self.heap)-1)
        root = self.heap.pop()
        self.heapifyDown(len(self.heap)-1)
        return root

    def heapifyUp(self, currIndex):
        if(currIndex == 0): return
        if(self.priorityGreater(currIndex, self.parent(currIndex))):
            self.swap(currIndex, self.parent(currIndex))
            self.heapifyUp(self.parent(currIndex))

    def heapifyDown(self, headIndex):
        """if(headIndex >= len(self.heap)-1):
            #We are done, it is the bottom
            #No children
            return"""
        left = self.left_child(headIndex)
        right = self.right_child(headIndex)
        if(left >= len(self.heap)):
            return
        if(right >= len(self.heap)):
            self.swap(headIndex,right)
            return
        if(priorityGreater(left, right)):
            self.swap(headIndex,left)
            self.swap(left,right)
        else:
            self.swap(headIndex,right)
        heapifyDown(right_child(headIndex))
    #Helper
    def right_child(self,i):
        return 2*i+2
    def left_child(self,i):
        return 2*i+1
    def parent(self,i):
        return i//2
    def swap(self, i,j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    def priorityGreater(self,i,j):
        I = self.heap[i]
        J = self.heap[j]
        return (self.max and (I.data > J.data)) or (not self.max and(I.data < J.data))