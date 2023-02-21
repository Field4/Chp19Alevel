# Linked list as nodes
class LinkedListNode:
    def __init__(self, value):
        self.__value = value
        self.__nextNode = None

    def insertval(self, val):  # inserts a new node into the linked list
        if self.__value == val:
            return "already inserted"
        elif self.__nextNode is None:
            self.__nextNode = LinkedListNode(val)
            return "inserted"
        elif self.__value < val < self.__nextNode.getvalue():
            temp = self.__nextNode
            self.setnextnode(LinkedListNode(val))
            self.__nextNode.setnextnode(temp)
            return "inserted"
        else:
            return self.__nextNode.insertval(val)

    def deletenode(self, val):  # deletes specified node from linked list
        if self.__value > val:
            return "Not in list"
        elif self.__value < val and self.__nextNode.getvalue() == val:
            self.__nextNode = self.__nextNode.getnextnode()
        elif self.__value < val and self.__nextNode is not None:
            return self.__nextNode.deletenode(val)
        else:
            return "Not in list"

    def setnextnode(self, node):
        self.__nextNode = node

    def getnextnode(self):
        return self.__nextNode

    def getvalue(self):
        return self.__value

    def printlist(self):
        print(self.__value)
        if self.__nextNode is not None:
            self.__nextNode.printlist()

    def find(self, val):  # finds specified value in linked list
        if self.__value == val:
            return "found"
        elif self.__value > val:
            return "not found"
        elif self.__value < val and self.__nextNode is not None:
            return self.__nextNode.find(val)
        else:
            return "not found"


# Binary tree as Nodes
class BinaryNode:
    def __init__(self, g_val):
        self.__val = g_val
        self.__left = None
        self.__right = None

    def insert(self, value):
        if value == self.__val:
            return "already inserted"
        elif value < self.__val:
            if self.__left is None:
                self.__left = BinaryNode(value)
                return "inserted"
            else:
                return self.__left.insert(value)
        else:
            if self.__right is None:
                self.__right = BinaryNode(value)
                return "inserted"
            else:
                return self.__right.insert(value)

    def search(self, value):
        if value == self.__val:
            return "found"
        elif value < self.__val:
            if self.__left is None:
                return "not found"
            else:
                return self.__left.search(value)
        else:
            if self.__right is None:
                return "not found"
            else:
                return self.__right.search(value)

    def nodeprint(self):
        if self.__left:
            self.__left.nodeprint()
        print(self.__val)
        if self.__right:
            self.__right.nodeprint()


# Stack class definition
class Stack:
    def __init__(self):
        self.__array = []
        self.__top = -1
        self.__full = 10

    def pushvalue(self, val):
        if self.__top == self.__full - 1:
            return "Stack full"
        else:
            self.__top += 1
            self.__array[self.__top] = val
            return "Push successful"

    def popvalue(self):
        if self.__top == -1:
            return "Stack empty"
        else:
            popped = self.__array.pop(self.__top)
            self.__top -= 1
            return popped

    def getstack(self):
        return self.__array


# Queue class definition
class Queue:
    def __init__(self):
        self.__array = ["" for i in range(10)]
        self.__front = -1
        self.__end = 0
        self.__size = 0
        self.__maxsize = 10

    def enqueue(self, val):
        if self.__size < self.__maxsize:
            if self.__end < 9:
                self.__end += 1
            else:
                self.__end = 0
            self.__size += 1
            self.__array[self.__end] = val
            return "Enqueued"
        else:
            return "queue is full"

    def dequeue(self):
        if self.__size == 0:
            return "queue is empty"
        else:
            item = self.__array[self.__front]
            if self.__front == len(self.__array) - 1:
                self.__front = 0
            else:
                self.__front += 1
        self.__size -= 1
        return item

    def getqueue(self):
        return self.__array




# Stack Array definition
stack = ["" for i in range(10)]
top = -1
stackfull = 10


def stackpush(val):
    global stack, top,stackfull
    if top == stackfull - 1:
        return "Stack full"
    else:
        top += 1
        stack[top] = val
        return "Push successful"


def stackpop():
    global stack, top
    if top == -1:
        return "Stack empty"
    else:
        popped = stack.pop(top)
        top -= 1
        return popped


# Queue array definition
queue = ["" for i in range(10)]
front = 0
end = 0
maxsize = 10
size = 0


def enqueue(val):
    global queue, front, end, maxsize, size
    if size < maxsize:
        if end < 9:
            end += 1
        else:
            end = 0
        size += 1
        queue[end] = val
        return "Enqueued"
    else:
        return "queue is full"


def dequeue():
    global queue, front, end, maxsize, size
    if size == 0:
        return "queue is empty"
    else:
        item = queue[front]
        if front == len(queue) - 1:
            front = 0
        else:
            front += 1
    size -= 1
    return item
