import queue

class TimesNode:
    def __init__(self, left, right):
        self.left = left
        self.right = right
        
    def eval(self):
        return self.left.eval() * self.right.eval()
    
    def inorder(self):
        return "(" + self.left.inorder() + " * " + self.right.inorder() + ")" 
    
class PlusNode:
    def __init__(self, left, right):
        self.left = left
        self.right = right
        
    def eval(self):
        return self.left.eval() + self.right.eval()
    
    
    def inorder(self):
        return "(" + self.left.inorder() + " + " + self.right.inorder() + ")"  
    
class NumNode:
    def __init__(self, num):
        self.num = num
        
    def eval(self):
        return self.num
    
    def inorder(self):
        return str(self.num)
 
def E(q):
    if q.isEmpty():
        raise ValueError("Invalid Prefix Expression")
    
    token = q.dequeue()
    
    if token == "+":
        return PlusNode(E(q),E(q))
    
    if token == "*":
        return TimesNode(E(q),E(q))
    
    return NumNode(float(token))
    
def main():
    num1 = NumNode(5)
    num2 = NumNode(4)
    num3 = NumNode(3)
    num4 = NumNode(2)
    t1 = TimesNode(num1, num2)
    t2 = TimesNode(num3, num4)
    root = PlusNode(t1, t2)
    print('Result:', root.eval())
    
        
    
if __name__ == "__main__":
    main()
