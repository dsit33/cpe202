#Problem 4: Complete the LinkedList datatype by implementing the delete, equality,
#iterate, length, and membership operations. Make sure they have the complexity 
#given in the LinkedList complexities table. Then, implement a test program in 
#your main function to thorougly test the operations you implemented. Call the 
#module linkedlist.py so that you can import this into other programs that may need it.

class LinkedList:

    class __Node:

        def __init__(self,item,next=None): 
            self.item = item 
            self.next = next
    
        def getItem(self): 
            return self.item

        def getNext(self): 
            return self.next

        def getNext(self): 
            return self.next

        def setNext(self,next): 
            self.next = next
            
    def __init__(self, contents = []):
        self.first = LinkedList.__Node(None, None)
        self.last = self.first
        self.numItems = 0
        
        for e in contents:
            self.append(e)
    
    def __getitem__(self,index):
        if index >= 0 and index < self.numItems:
            cursor = self.first.getNext()
            for i in range(index):
                cursor = cursor.getNext() 
                        
        return cursor.getItem()
            
    def __setItem__(self, index, val):
        if index >= 0 and index < self.numItems:
            cursor = self.first.getNext()
            for i in range(index):
                cursor = cursor.getNext()
                
            cursor.setItem(val)
            return
        raise IndexError("LinkedList assignment index out of range")
    
    def __add__(self, other):
        if type(self) != type(other):
            raise TypeError("Concatenate undefined for " + str(type(self)) + " + " + str(type(other)))
        
        result = LinkedList()
        cursor = self.first.getNext()
        
        while cursor != None:
            result.append(cursor.getItem())
            cursor = cursor.getNext()
            
        cursor = other.first.getNext()
        
        while cursor != None:
            result.append(cursor.getItem())
            cursor = cursor.getNext()
            
        return result
    
    def append(self, item):
        node = LinkedList.__Node(item)
        self.last.setNext(node)
        self.last = node
        self.numItems += 1
        
    def insert(self, index, item):
        cursor = self.first
        
        if index < self.numItems:
            for i in range(index):
                cursor = cursor.getNext()
                
            node = LinkedList.__Node(item, cursor.getNext())
            cursor.setNext(node)
            self.numItems += 1
        else:
            self.append(item)
                        
    def __delitem__(self, index):
        count = 0
        prevNode = self.first
        while count < index - 1:
            prevNode == prevNode.getNext()
            count += 1
        currentNode = prevNode.getNext()
        prevNode.next = currentNode.getNext()
        
    
    def __eq__(self, other):
        for i in range(len(self)):
            if self.getItem(i) != other.getItem(i):
                return False
        return True
    
    def __iter__(self):
        def next(self):
            if self.__Node is None:
                raise StopIteration
            else:
                currentNode = self.__Node
                self.__Node = self.__Node.getNext()
                return currentNode
            
    def __len__(self):
        length = 0
        if self.first != None:
            length = 1
        currentNode = self.first.getNext()
        while currentNode != self.first:
            currentNode = currentNode.getNext()
            length += 1
            
        return length
        
    def __contains__(self, item):
        currentNode = self.first
        while currentNode.getNext() != self.first:
            if currentNode.getItem() == item:
                return True
            currentNode = currentNode.getNext()
            
        if self.last.getItem() == item:
            return True
        return False


"""    testLst = LinkedList()
    testLst2 = LinkedList()
    for i in range(10):
        testLst.append(i)
        testLst2.append(i)
    if testLst != testLst2:
        print(Eq Test Failed)
    
    del testLst(1)
    if testLst == testLst2:
        print(Del Test Failed)
        """
    
    
    