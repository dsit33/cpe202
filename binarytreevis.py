"""
Instructor: Hollister
Derek Sit
Project 3 binarytreevis
"""
import turtle
import tkinter.messagebox
import tkinter

class BinarySearchTree():

	class __Node():
		def __init__(self,val,left=None,right=None):
			self.val = val
			self.left = left
			self.right = right

		def getVal(self):
			return self.val

		def setVal(self, item):
			self.val = item

		def getLeft(self):
			return self.left

		def getRight(self):
			return self.right

		def setLeft(self,item):
			self.left = item

		def setRight(self,item):
			self.right = item

		def __iter__(self):
			if self.left != None:
				for elem in self.left:
					yield elem

			yield self.val

			if self.right != None:
				for elem in self.right:
					yield elem

	def __init__(self,contents=None):
		self.root = None
		if contents != None:
			for elem in contents:
				self.insert(float(elem))


	def insert(self,val):
		def __insert(root,val):
			if root == None:
				return BinarySearchTree.__Node(val)

			if val < root.getVal():
				root.setLeft(__insert(root.getLeft(),val))
			else:
				root.setRight(__insert(root.getRight(),val))

			return root

		if val not in self:
			self.root = __insert(self.root,float(val))

	def __iter__(self):
		if self.root != None:
			return self.root.__iter__()
		else:
			return [].__iter__()

	def __contains__(self,item):
		for elem in self:
			if elem == float(item):
				return True
		return False

	def getLevel(root,value,level):
		if root == None:
			return 0
		if root.getVal() == value:
			return level
		if root.getLeft() != None or root.getRight() != None:
			return BinarySearchTree.getLevel(root.getLeft(),value,level+1) + BinarySearchTree.getLevel(root.getRight(),value,level+1)
		return 0

	def numOfLevels(root):
		if root == None:
			return 0
		else:
			lDepth = BinarySearchTree.numOfLevels(root.getLeft())
			rDepth = BinarySearchTree.numOfLevels(root.getRight())
			if lDepth > rDepth:
				return lDepth + 1
			else:
				return rDepth + 1

	def delete(self,val):

		def getRightMost(root):
			current = root
			while current.getRight() != None:
				current = current.getRight()
			return current

		def __delete(root,val):
			if root == None:
				return root
			if val < root.getVal():
				root.setLeft(__delete(root.getLeft(),val))
			elif val > root.getVal():
				root.setRight(__delete(root.getRight(),val))
			else:
				if root.getLeft() == None:
					temp = root.getRight()
					root.setVal(None)
					return temp
				elif root.getRight() == None:
					temp = root.getLeft()
					root.setVal(None)
					return temp
				temp = getRightMost(root.getLeft())
				root.setVal(temp.getVal())
				root.setLeft(__delete(root.getLeft(),temp.getVal()))
			return root
		if val in self:
			self.root = __delete(self.root,float(val))

	def inorder(self):
		lst = []
		for item in self:
			lst.append(item)
		return lst

	def preorder(self):

		def __preorder(root):
			lst.append(root.getVal())
			if root.getLeft() != None:
				__preorder(root.getLeft())
			if root.getRight() != None:
				__preorder(root.getRight())
		lst = []
		__preorder(self.root)
		return lst

	def postorder(self):

		def __postorder(root):
			if root.getLeft() != None:
				__postorder(root.getLeft())
			if root.getRight() != None:
				__postorder(root.getRight())
			lst.append(root.getVal())
		lst = []
		__postorder(self.root)
		return lst

	def levelorder(self):
		lst = []
		currentLevel = [self.root]
		while currentLevel:
			nextLevel = list()
			for item in currentLevel:
				lst.append(item.getVal())
				if item.getLeft() != None:
					nextLevel.append(item.getLeft())
				if item.getRight() != None:
					nextLevel.append(item.getRight())
			currentLevel = nextLevel
		return lst

class Vis(tkinter.Frame):

	def __init__(self,master=None):
		super().__init__(master)
		self.pack()
		self.buildWindow()

	def buildWindow(self):
		tree = BinarySearchTree()
		self.master.title("Binary Tree Visualization")
		cv = tkinter.Canvas(self,width=600,height=600)
		cv.pack(side=tkinter.LEFT)

		t = turtle.RawTurtle(cv)
		scr = t.getscreen()
		scr.tracer(100000)
		scr.setworldcoordinates(0,0,300,300)
		scr.bgcolor("white")
		scr.tracer(0)
		t.ht()
		t.pu()

		def drawTree():
			scr.clear()
			scr.tracer(1000000)
			scr.setworldcoordinates(0,0,300,300)
			scr.bgcolor("white")
			scr.tracer(0)
			t = turtle.RawTurtle(cv)
			t.ht()
			t.pu()
			t.width(1)
			t.color("black")

			inorder = tree.inorder()
			xOffset = 300/len(inorder)
			yOffset = 300/(BinarySearchTree.numOfLevels(tree.root)+1)
			t.penup()
			a = 0
			x = 0
			y = 0
			for i in range(len(inorder)):
				oldX = x
				oldY = y
				x = a * xOffset + xOffset/2
				a += 1
				y = ((BinarySearchTree.numOfLevels(tree.root)+1) - BinarySearchTree.getLevel(tree.root,inorder[i],1)) * yOffset + yOffset/2
				t.goto(x,y)
				t.dot()
				t.write(inorder[i],align="center",font=("Arial",8,"normal"))
				t.pendown()
				if BinarySearchTree.getLevel(tree.root,inorder[i],1) > BinarySearchTree.getLevel(tree.root,inorder[i-1],1) and oldX != 0:
					t.penup()
					t.goto(oldX,oldY)
					t.pendown()

		sideBar = tkinter.Frame(self,padx=5,pady=25)
		sideBar.pack(side=tkinter.RIGHT,fill=tkinter.BOTH)

		quitButton = tkinter.Button(sideBar,text="Quit",command=self.master.quit)
		quitButton.pack(fill=tkinter.BOTH)

		nodeLabel = tkinter.Label(sideBar,text="Node Value:")
		nodeLabel.pack()

		nodeValue = tkinter.StringVar()
		nodeEntry = tkinter.Entry(sideBar,textvariable=nodeValue)
		nodeEntry.pack()

		def insHandler():
			tree.insert(nodeValue.get())
			drawTree()


		def rmvHandler():
			tree.delete(nodeValue.get())
			drawTree()
		

		def containsHandler():
			if nodeValue.get() in tree:
				tkinter.messagebox.showwarning("Search lsts","Item is in tree!")
			else:
				tkinter.messagebox.showwarning("Search lsts","Item is NOT in tree!")

		insButton = tkinter.Button(sideBar,text="Insert",command=insHandler)
		insButton.pack(fill=tkinter.BOTH)

		rmvButton = tkinter.Button(sideBar,text="Remove",command=rmvHandler)
		rmvButton.pack(fill=tkinter.BOTH)
		
		containsButton = tkinter.Button(sideBar,text="Contains?",command=containsHandler)
		containsButton.pack(fill=tkinter.BOTH)


def main():
	root = tkinter.Tk()
	app = Vis(root)
	app.mainloop()

if __name__ == '__main__':
	main()
