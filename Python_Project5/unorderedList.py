class UnorderedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def isEmpty(self):
        return self.head == None

    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
        self.length += 1
    
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
        #I need to find where the actual node is removed and decrement self.length by 1 there
        while current != None and not found:
            if current.getData() == item:
                found = True
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
    def append(self,item):
        current = self.head
        if current:
            while current.getNext() != None:
                current = current.getNext()
            current.setNext(Node(item))
        else:
            self.head = Node(item)
    
    def printList(self):
        node = self.head
        while node:
            print (node.value)
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