#Problem 7: Implement a stack data type using a linked list implementation. 
#Create a set of test cases to throroughly test your datatype. Place the 
#datatype in a file called stack.py and create a main function that runs your 
#test cases.

import linkedlist

class Stack(linkedlist.LinkedList):
        
    def pop(self):
        if self.isEmpty():
            raise RunTimeError("Attempt to pop an empty stack")
        self.__delitem__(len(self)-1)
        
    def push(self, item):
        self.append(item)
        
    def top(self):
        if self.isEmpty():
            raise RunTimeError("Attempt to get top of empty stack")
        
        return self.last
    
    def isEmpty(self):
        if self.first.getItem() == 0:
            return True
        else:
            return False
        

def main(): 
    s = Stack()
    lst = list(range(10)) 
    lst2 = []
    
    for k in lst: 
        s.push(k)
        
    if s.top() == 9: 
        print("Test 1 Passed")
    else: 
        print("Test 1 Failed")
        
    while not s.isEmpty(): 
        lst2.append(s.pop())
        
    lst2.reverse()
    
    if lst2 != lst: 
        print("Test 2 Failed")
    else: 
        print("Test 2 Passed")
        
if __name__ == '__main__':
    main()