class Node:
    def __init__(self, data, nextNode = None):
        self.data = data
        self.nextNode = nextNode


node1 = Node(1)
node2 = Node(2)
node3 = Node(6)
node4 = Node(24)

node1.nextNode = node2
node2.nextNode = node3
node3.nextNode = node4

def printNextNodes(Node):
    currentNode = Node
    while currentNode != None:
        print(currentNode.data)
        currentNode = currentNode.nextNode
    print(currentNode)

printNextNodes(node1)