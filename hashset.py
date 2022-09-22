import random

class HashSet:
    class __Placeholder:
        def __init__(self):
            pass
        
        def __eq__(self,other):
            return False
        
    def __add(item,items):
        idx = hash(item) % len(items)
        loc = -1
        
        while items[idx] != None:
            if items[idx] == item:
                # item already in set
                return False
            
            if loc < 0 and type(items[idx]) == HashSet.__Placeholder:
                loc = idx
                
            idx = (idx + 1) % len(items)
            
        if loc < 0:
            loc = idx
            
        items[loc] = item  
        
        return True
    
    def __remove(item,items):
        idx = hash(item) % len(items)
        
        while items[idx] != None:
            if items[idx] == item:
                nextIdx = (idx + 1) % len(items)
                if items[nextIdx] == None:
                    items[idx] = None
                else:
                    items[idx] = HashSet.__Placeholder()
                return True
            
            idx = (idx + 1) % len(items)
            
        return False
        
    def __rehash(oldList, newList):
        for x in oldList:
            if x != None and type(x) != HashSet.__Placeholder:
                HashSet.__add(x,newList)
                
        return newList
    
    def __init__(self,contents=[]):
        self.items = [None] * 10
        self.numItems = 0
        
        for item in contents:
            self.add(item)
          
    def __str__(self):
        lst = "["
        for item in self.items:
            lst += "{}, ".format(item)
        return lst
    
    def __iter__(self):
        for i in range(len(self.items)):
            if self.items[i] != None and type(self.items[i]) != HashSet.__Placeholder:
                yield self.items[i]    
    
    # Following are the mutator set methods 
    def add(self, item):
        if HashSet.__add(item,self.items):
            self.numItems += 1             
            load = self.numItems / len(self.items)
            if load >= 0.75:
                self.items = HashSet.__rehash(self.items,[None]*2*len(self.items))
    def remove(self, item):
        if HashSet.__remove(item,self.items):
            self.numItems -= 1
            load = max(self.numItems, 10) / len(self.items)
            if load <= 0.25:
                self.items = HashSet.__rehash(self.items,[None]*int(len(self.items)/2))
        else:
            raise KeyError("Item not in HashSet")
        
    def discard(self, item):
        try:
            self.remove(item)
        except:
            pass
        
    def pop(self):
        index = random.randint(0, len(self.items))
        item = self.items[index]
        self.discard(item)
            
    def clear(self):
        self.items = [None]*10
        self.numItems = 0
        
    def update(self, other):
        for x in other:
            self.add(x)
            
    def intersection_update(self, other):
        for x in self.items:
            if x not in other:
                self.discard(x)
        return self.items
            
    def difference_update(self, other):
        for item in other:
            self.discard(item)
        return self.items
                
    def symmetric_difference_update(self, other):
        for x in other:
            if x not in self.items:
                self.add(x)
        return self.items
                
    # Following are the accessor methods for the HashSet  
    def __len__(self):
        return self.numItems
    
    def __contains__(self, item):
        idx = hash(item) % len(self.items)
        while self.items[idx] != None:
            if self.items[idx] == item:
                return True
            
            idx = (idx + 1) % len(self.items)
            
        return False
    
    # One extra method for use with the HashMap class. This method is not needed in the 
    # HashSet implementation, but it is used by the HashMap implementation. 
    def __getitem__(self, item):
        pass
        
    def not__contains__(self, item):
        idx = hash(item) % len(self.items)
        while self.items[idx] != None:
            if self.items[idx] == item:
                return False
            
            idx = (idx + 1) % len(self.items)
            
        return True
    
    def isdisjoint(self, other):
        for x in other:
            if self.__contains(x):
                return False
        return True
    
    def issubset(self, other):
        return other in self
    
    def issuperset(self, other):
        return self in other
    
    def union(self, other):
        newItems = []
        for x in self.items:
            newItems.append(x)
        for y in other:
            newItems.append(y)
        return HashSet(newItems)
    
    def intersection(self, other):
        return HashSet(self.intersection_update(other))
    #done
    def difference(self, other):
        return HashSet(self.difference_update(other))
    
    def symmetric_difference(self, other):
        return HashSet(self.symmetric_difference_update(other))
    
    def copy(self):
        return HashSet.__init(self.items)
    
    # Operator Definitions
    def __or__(self, other):
        pass
    
    def __and__(self,other):
        pass
    
    def __sub__(self,other):
        pass
    
    def __xor__(self,other):
        pass
    
    def __ior__(self,other):
        pass
    
    def __iand__(self,other):
        pass
    
    def __ixor(self,other):
        pass    
    
    def __le__(self,other):
        pass
    
    def __lt__(self,other):
        pass
    
    def __ge__(self,other):
        pass
    
    def __gt__(self,other):
        pass
    
    def __eq__(self,other):
        pass
    
    

def main():
    s = HashSet(list(range(100)))
    
    t = HashSet(list(range(10,20)))
    
    u = HashSet(list(range(10,20)))
    
    if len(t) == len(u) and len(t) == 10:
        print("Test 1 Passed")
    else:
        print("Test 1 Failed")
        
    s.intersection_update(t)
    
    if len(s) == 10:
        print("Test 2 Passed")
    else:
        print("Test 2 Failed")
        
    s = HashSet(list(range(100)))
    
    t.update(s)
    
    if len(s) == len(t):
        print("Test 3 Passed")
    else:
        print("Test 3 Failed")
        
    t.clear()
    t.update(u)
    
    if len(t) == len(u):
        print("Test 4 Passed")
    else:
        print("Test 4 Failed")
        
    s.difference_update(t)
    
    test5Passed = True
    test6Passed = True
    
    for x in range(1,10):
        if x in s:
            pass
        else:
            test5Passed = False
            print("Test 5 Failed on",x)
            
        if x not in s:
            test6Passed = False
            print("Test 6 Failed on",x)
            
    if test5Passed:
        print("Test 5 Passed")
    
    if test6Passed:
        print("Test 6 Passed")
        

    test7Passed = True
    test8Passed = True
    
    for x in range(20,100):
        if x in s:
            pass
        else:
            test7Passed = False
            print("Test 7 Failed on",x)
            
        if x not in s:
            test8Passed = False
            print("Test 8 Failed on",x)
            
    if test7Passed:
        print("Test 7 Passed")
    
    if test8Passed:
        print("Test 8 Passed")   
        
    x = HashSet(["a","b","c","d","e","f","g","h","i","j","k"])
    
    y = HashSet(["c","d","e","l","m","n"])

   
    
if __name__ == "__main__":
    main()