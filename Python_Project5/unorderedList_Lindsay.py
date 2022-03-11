# Course: CSCI 356, Section 1
# Student Name: Drew Lindsay
# Student ID: 10725791
# Program 5
# Due Date: 3/11/2022
# In keeping with the Honor Code of UM, I have neither given nor received inappropriate assistance
# from anyone other than the TA or instructor.
# Program Description:This program implements a linked list that is unordered, can print based on a count that is a constructor,
# and has an append method to allow values to be tacked on to the end of the list

class UnorderedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def isEmpty(self):
        return self.head == None

    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
        self.length += 1
        if self.length == 1:
            self.tail = temp
    
    def size(self):
        return self.length

    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
                self.length -= 1
            else:
                previous = current
                current = current.getNext()
        if not found:
            return
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    #This is O(n) and needs to be O(1)
    def oldappend(self,item):
        current = self.head
        if current:
            while current.getNext() != None:
                current = current.getNext()
            current.setNext(Node(item))
            self.length +=1
        else:
            self.head = Node(item)
            self.tail = Node(item)
            self.length +=1
    
    def append(self,item):
        current = self.tail
        new = Node(item)
        if current:
            current.setNext(Node(item))
            self.length +=1
            self.tail = current.getNext()
        else:
            self.head = Node(item)
            self.tail = Node(item)
            self.length +=1
    
    def printList(self):
        node = self.head
        while node:
            print (node.data, end=' ')
            node = node.next

class Node(object):
    def __init__(self,initdata):
        self.data = initdata
        self.next = None
    
    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata
    
    def setNext(self,newnext):
        self.next = newnext