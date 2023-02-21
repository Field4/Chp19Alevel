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


# Test for Linked List
root = LinkedListNode(5)
root.insertval(6)
root.insertval(8)
root.insertval(7)
root.printlist()
root.deletenode(7)
print("7 deleted")
root.printlist()
