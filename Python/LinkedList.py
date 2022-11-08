class Node:
    def __init__(self, value, nextNode = None):
        self.value = value
        self.nextNode = nextNode

class LinkedList:
    
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None
    def append(self, value):
        newNode = Node(value)
        self.length += 1
        if self.head == None:               # for 1st Node
            self.head = newNode
            return
        if self.head.nextNode == None:      # for 2nd Node
            self.head.nextNode = newNode
            self.tail = newNode
            return
        
        self.tail.nextNode = newNode        
        self.tail = newNode
        
    def remove(self, value):
        self.length -= 1
        if self.head.value == value:
            self.head = self.head.nextNode
            return
        prevNode = self.head
        currNode = prevNode.nextNode
        while currNode != None:
            if currNode.value == value:
                prevNode.nextNode = currNode.nextNode
                return
            prevNode = currNode
            currNode = currNode.nextNode
        self.length += 1
        return

    def insert(self, value, index = 0):
        if index >= self.length:
            print("Index out of bound")
            return
        self.length += 1
        newNode = Node(value)
        if index == 0:
            newNode.nextNode = self.head
            self.head = newNode
            return
        i = 1
        currNode = self.head.nextNode
        prevNode = self.head
        while i != index:
            prevNode = currNode
            currNode = currNode.nextNode
            i += 1
        prevNode.nextNode = newNode
        newNode.nextNode = currNode
        return
    
    def __str__(self):
        mystr = ""
        currNode = self.head
        while currNode != None:
            mystr = mystr + ', ' + str(currNode.value)
            currNode = currNode.nextNode
        return '[' + mystr[2:] + ']' 

    def __len__(self):
        return self.length


# Testing

llist = LinkedList()

llist.append(4)
llist.append(7)
llist.append(8)
llist.append(10)
llist.append(13)
llist.append(17)

print(llist)
print(len(llist))

llist.insert(45, 1)
print(llist)
print(len(llist))

llist.remove(10)
llist.remove(17)
llist.remove(15)
print(llist)
print(len(llist))


