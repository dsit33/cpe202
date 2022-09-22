import priorityqueue


class Node:
   def __init__(self, freq, char, left, right):
      self.freq = freq
      self.char = char
      self.left = left
      self.right = right

def huffman(x):
   Q = priorityqueue.PriorityQueue()
   visited = []
    
   for char in x:
      if char not in visited:
         visited.append(char)
         fre = frequency(char, x)
         T = Node(fre, char, None, None)
         Q.enqueue(T, fre)
      
   while len(Q) > 1:
      T1 = Q.dequeue()
      T2 = Q.dequeue()
      fre = T1.freq + T2.freq
      newTree = Node(fre, None, T1, T2)
      Q.enqueue(newTree, fre)
   
   final = Q.dequeue()
   return final
         
      
def frequency(char, word):
   return 1 - word.count(char)/len(word)

def get_huffman_code(char, root):
   
   def getCode(char, root, code):
      if root.right != None:
         if root.right.char != char:
            return getCode(char, root.left, code + '1')
         return code + '0'
      return code
   code = ""
   return getCode(char, root, code)
       