class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def put(self, item):
        if(type(item) != int):
		print
	else:
		self.items.insert(0,item)

    def get(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
