class Stack():
	def __init__(self):
		self.stack = []

	def push(self, num):
		return self.stack.appen(num)

	def pop(self):
		return self.stack.pop()

	def checkSizze(self):
		return len(self.stack)
