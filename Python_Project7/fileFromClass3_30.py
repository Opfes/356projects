class HashTable:
    def init (self, size) :
        self.slots = [i for i in range (size)]
        self.data = [None] * size

    def store (self, key):
        hashValue = self.hashFunction (key, len(self.slots))
        if self.data (hashValue) == None:
            self.data[hashValue] = key
        else:
            nextSlot = self. rehash(hashValue, len(self.slots))
            while self.data[nextSlot] != None:
                nextSlot = self.rehash(nextSlot, len(self.slots))
            self.data[nextSlot] = key

    def hashFunction (self, key, size) :
        return key % size
    
    def hashFunction2 (self, key, size):
        strKeySquare = str(key * key)
        length = len(strKeySquare)
        midDigit = strKeySquare[(0+length-1)//2]
        mid2Digit = int(strKeySquare[(0+length-1)//2+1])

        if length % 2 == 0:
            return (midDigit*10 + mid2Digit) % size
        else:
            return midDigit % size

    def rehash (self, oldHash, size):
        return (oldHash+1) % size

    def search(self, key):
        found = False
        hashValue = self.hashFunction(key, len(self.slots))
        if key == self.data[hashValue]:
            found = True
        return found
        