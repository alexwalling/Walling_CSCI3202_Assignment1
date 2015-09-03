class Node():
	def __inint__(self, val, left, right, parent):
		self.val = val
		self.right = right
		self.left = left
		self.parent = parent

class BinaryTree():
	def __init__(self):
		self.root = None

	def add(self, val, parentVal):
		if (self.root == None):
			self.root = Node(value, None, None, None)
		else:
			head = self.getNode(self.root, parentVal)

			if (head.left == None):
				if (head.right == None):
					head.left = None(val, None, None, head)
			else:
				if(head.right == None):
					head.right = Node(val, None, None, head)
				else:
					print "Parent has two children, node not added"
					return False

	def printTree(self):
		head = self.root
		if (head == None):
			print "Empty Tree"
		else:
			self.printRec(head.left)
			self.printRec(head.right)
	
	def printRec(self, head):
		if (head != None):
			print head.value
			self.printRec(head.left)
			self.printRec(head.right)

	def delete(self, value):
		head = self.getNode(self.root, value)
		if (head.parent.left.value == head.value):
			head.parent.left = None
		else:
			head.parent.right = None

	def getNode(self, head, val):
		if(head == None):
			return False
		elif (head.val == val):
			return head
		else:
			if (head.left == None):
				return False
			else:
				if (head.right == None):
					return self.getNode(head.left, val)
				else:
					return self.getNode(head.left, val) or self.getNode(head.right, val)
