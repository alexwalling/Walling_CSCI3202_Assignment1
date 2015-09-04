class Graph():

	graph = {}

	def addVertex(self, val):
		if val in self.graph:
			print "Vertex already exists"
		else:
			self.graph[val] = []	

	def addEdge(val1, val2):
		if val1 not in self.graph or val2 not in self.graph:
			print "one or both values not in graph"
		else:
			self.graph[val1].append(val2)
			self.graph[val2].append(val1)

	def findVertex(val)
		vertex = self.graph[val]
		if (vertex == None):
			print "Vertex not found"
			return "no vertex"
		else:	
			print "vertex with value %s has verticies %s" % (val, vertex)
			return vertex
