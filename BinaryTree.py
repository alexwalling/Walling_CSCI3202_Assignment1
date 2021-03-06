class Node():
	def __init__(self, val, left, right, parent):
		self.val = val
		self.right = right
		self.left = left
		self.parent = parent

class BinaryTree():
	def __init__(self):
		self.root = None

	def add(self, val, parentVal):
		if (self.root == None):
			self.root = Node(val, None, None, None)
		else:
			head = self.getNode(self.root, parentVal)

			if (head.left == None):
				if (head.right == None):
					head.left = Node(val, None, None, head)
			else:
				if(head.right == None):
					head.right = Node(val, None, None, head)
				else:
					print "Parent has two children, node not added"
					return False

	def printTree(self):
		head = self.root
		print head.val
		if (head == None):
			print "Empty Tree"
		else:
			self.printRec(head.left)
			self.printRec(head.right)
	
	def printRec(self, head):
		if (head != None):
			print head.val
			self.printRec(head.left)
			self.printRec(head.right)

	def delete(self, val):
		head = self.getNode(self.root, val)
		if (head.parent.left.val == head.val):
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
