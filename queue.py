#Problem 5:Implement a queue data type using a linked list implementation. Create a set 
#of test cases to throroughly test your datatype. Place the datatype in a file 
#called queue.py and create a main function that runs your test cases.

import linkedlist

class Queue(linkedlist.LinkedList):
    
    def dequeue(self):
        if self.isEmpty():
            raise RunTimeError("Attempt tp dequeue an empty queue")
        self.__delitem__(self.__len__() - 1)
        
    def enqueue(self, item):
        self.append(item)
        
    def front(self):
        return self.last
    
    def isEmpty(self):
        if self.first.getItem() == 0:
            return True
        else:
            return False