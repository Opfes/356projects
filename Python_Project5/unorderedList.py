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

