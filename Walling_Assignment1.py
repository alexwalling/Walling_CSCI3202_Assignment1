from BinaryTree import BinaryTree
from BinaryTree import Node
from Graph import Graph
from MyQueue import MyQueue
from Stack import Stack
from Queue import Queue

def QueueTest(q):
	print "---------------------------------------"
	print "Beginning Queue Test"
	print "---------------------------------------"
	for i in range (11):
		q.put(i)
	print("0-10 in Queue")
	print("Size %d" % q.size())
	print("Dequeuing")
	for j in range(11):
		print("dequeuing: %s = " % j), q.get() == j 

def stackTest(stack):
	print "---------------------------------------"
	print "Beginning Stack Test"
	print "---------------------------------------"
	for i in range(11):
		stack.push(i)
	print "0-10 have been added to stack"
	print "printing popping off"
	for i in range(11):
		print stack.pop()
	
def TreeTest(tree):
	print "---------------------------------------"
	print "Beginning Tree Test"
	print "---------------------------------------"
	tree.add(1, None)
	tree.add(2, 1)
	tree.add(3, 1)
	tree.add(4, 2)
	tree.add(5, 2)
	tree.add(6, 3)
	tree.add(7, 3)
	tree.add(8, 4)
	tree.add(9, 4)
	tree.add(10, 5)
	print "tree is built"
	tree.printTree()
	print "delete from tree 10 and 7"
	tree.delete(10)
	tree.delete(7)
	tree.printTree()

def GraphTest(graph):
	print "---------------------------------------"
	print "Beginning Graph Test"
	print "---------------------------------------"
	for i in range(11):
		graph.addVertex(i)
	graph.addEdge(1,2)
	graph.addEdge(1,8)
	graph.addEdge(3,8)
	graph.addEdge(3,1)
	graph.addEdge(3,5)
	graph.addEdge(4,2)
	graph.addEdge(4,1)
	graph.addEdge(4,7)
	graph.addEdge(5,6)
	graph.addEdge(5,8)
	graph.addEdge(6,10)
	graph.addEdge(7,1)
	graph.addEdge(7,3)
	graph.addEdge(7,6)
	graph.addEdge(8,4)
	graph.addEdge(8,10)
	graph.addEdge(9,7)
	graph.addEdge(9,6)
	graph.addEdge(10,2)
	graph.addEdge(10,9)
	print("added edges")
	graph.findVertex(2)
	graph.findVertex(4)
	graph.findVertex(5)
	graph.findVertex(7)
	graph.findVertex(9)


q = Queue()
QueueTest(q)
stack = Stack()
stackTest(stack)
tree = BinaryTree()
TreeTest(tree)
graph = Graph()
GraphTest(graph)
