# Course: CSCI 356, Section 1
# Student Name: Drew Lindsay
# Student ID: 10725791
# Program 5
# Due Date: 3/11/2022
# In keeping with the Honor Code of UM, I have neither given nor received inappropriate assistance
# from anyone other than the TA or instructor.
# Program Description:This program implements a linked list that is unordered, can print based on a count that is a constructor,
# and has an append method to allow values to be tacked on to the end of the list

#constructor for the unordered list class
class UnorderedList:
    def __init__(self):
        #constructors for the head, tail, and length values so they can be modified in the other functions
        self.head = None
        self.tail = None
        self.length = 0

    #check if the list is empty based on whether or not there is a head value
    def isEmpty(self):
        return self.head == None

    #add function
    def add(self,item):
        #stores new value in temp variable
        temp = Node(item)
        #pushes the current head value back
        temp.setNext(self.head)
        #temp is now the head value
        self.head = temp
        #increments length and then sets the head to the tail if it is the first value
        self.length += 1
        if self.length == 1:
            self.tail = temp
    
    #size function just prints the value of the length
    def size(self):
        return self.length

    #search method to find if a value is present in the list
    def search(self,item):
        #starts at the head and assumes the found is false by default
        current = self.head
        found = False
        #loop to iterate through the list and change found to true if the value is located
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    #remove function to find the value passed and then remove it from the list
    def remove(self,item):
        #starts at the head of the list and assumes that found is false
        current = self.head
        previous = None
        found = False
        #iterates through the loop to find the passed value
        while current != None and not found:
            if current.getData() == item:
                found = True
                self.length -= 1
            else:
                previous = current
                current = current.getNext()
        #if not faund stop
        if not found:
            return
        #cases for if the value is found
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    #function to add values to the end of the list with complexity of 1    
    def append(self,item):
        #start at the edn of the list
        current = self.tail
        #if there is a value at the end of the list, set next, and then change the tail value, and increment the count
        if current:
            current.setNext(Node(item))
            self.length +=1
            self.tail = current.getNext()
        #otherwise, this is the first item in the list and should be both the head and the tail
        else:
            self.head = Node(item)
            self.tail = Node(item)
            self.length +=1
    
    #simple print function to iterate through the list and print the values starting at the head and printing data until there are
    #no more nodes
    def printList(self):
        node = self.head
        while node:
            print (node.data, end=' ')
            node = node.next

#Node class for the values in the list
class Node(object):
    def __init__(self,initdata):
        #data value for the number or whatever the node is holding, as well as the data for the next node
        self.data = initdata
        self.next = None
    
    #function to return the value held by the node
    def getData(self):
        return self.data

    #function to return the value after the current node
    def getNext(self):
        return self.next

    #function to change the value stored by the node
    def setData(self,newdata):
        self.data = newdata
    
    #function to change the node that is located after the current one
    def setNext(self,newnext):
        self.next = newnext