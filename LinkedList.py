#Building a Singly-Linked List
#Nodes are he building block for a list
#Calling a method: need parenthesis at the end: l.size()
#Every Python method should take self as an argument
#linked lists dont have index positions but we can mimic the
#behavior by just counting the number of times we access the next node

#creating 2 instance variables
class Node:
    """
    An object for storing a single node of a linked list.
    Models two attributes - data and the link to the next node in the list
    """

    data = None
    next_node = None
    #constructor to make this class easy to create
    def __init__(self, data):
        self.data = data
        
    def __repr__(self):
        return "<Node data: %s>" % self.data

# N1 = Node(10)
# print(N1)

# N2 = Node(20)
# N1.next_node = N2
# #N1 now points to N2
# print(N1.next_node)



"""
The head attribute models the only node the list will have
reference to
Since every node points to the next node, to find a particular
node we can go from one node to the next in a process called 
list traversal
In the class constructor here, we set the default value of head
to be none so that new lists created are always empty.
"""
class LinkedList:
    """
    Singly Linked List
    """
    #create an empty linked list
    def __init__(self):
        self.head = None

    #check if list is empty, evaluates to true
    def is_empty(self):
        return self.head == None

    #check the size of list
    def size(self):
        """
        Returns the number of nodes in the list by visiting
        every node 
        Takes linear time O(n)
        """
        current = self.head
        count = 0 #local variable
        
        #while current does not equal None
        while current:
            count += 1
            current = current.next_node

        return count
    
    def add(self, data):
        """
        Adds a new node containing data at the head of the 
        Takes O(1) time
        """
        #This insert operation is a reassignment of the head & next node properties -
        # this is a constant time operation O(1)
        #creates a new node to hold on the new data to be added
        #Before we set the new node as head of the list, we need to point
        #the node's next property at whatever node is currently at head
        #This way when we set a new node to be head of the list, 
        #we dont lose a reference to the old head
        new_node = Node(data)
        #if there was no node at head, this sets the next node to None
        new_node.next_node = self.head
        self.head = new_node #set new node as head of the list

    def search(self, key):
        """
        Search for the first node 
        containing data that matches the key
        Returns the node or None if not found
        Worst case scenario: checking every single node in the list or fail
        O(n) or linear time complexity
        """
        current = self.head

        #while current is not None
        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node

        return None

    def insert(self, data, index):
        """
        Inserts a new Node containing data at index position
        Insertion takes constant O(1) time but finding at the insertion point takes 
        linear time
        Therefore insertion takes overall linear O(n) time
        
        even tho we can easily insert a new node w/o having to shift
        the rest; ultimately adding to the head or tail of the linked list
        if you have a reference is much more efficient..
        """
        if index == 0:  
            self.add(data) #insert new node at start/head of linked list
        
        if index > 0:
            new = Node(data)

            position = index
            current = self.head

        #keep calling next node while reassigning the current node
        while position > 1:
            current = current.next_node
            position -= 1 #decrements 1.. loop exits & current will be 

        prev_node  = current
        next_node = current.next_node

        prev_node.next_node = new
        new.next_node = next_node

    """
    2 TYPES OF defining REMOVE METHODS:
    -Provide a key (data the node stores) to remove as an arguemnt
    -Provide an index 
    
    """

    def remove(self, key):
        """
        Removes node containing data that matches the key
        Returns the node or None if key doesnt exist
        Takes O(n) time (linear time) because it has to search the entire list
        in the worst case scenario
        """
        current = self.head #point to the head
        previous = None #keep track of the prev node
        found = False #serves as stopping condition

        #to keep track of the current node in the list as it traverses 
        #down to find the node that matches the key
        #loop will keep traversing the linked list as long as found is false;
        #meaning we havent found the key we are looking for
        #once we found the matching value, we set the found value to be true;
        #essentially ending the loop
        
        #WHILE current is not none, loop will continue executing
        #if current is None, this means we have gone past the tail node
        #the second condition asks the loop to continue evaluating as long as not found equals true
        #if either one condition evaluates to false, then the loop will terminate
        while current and not found:
            #1st scenario: key matches the data in the node
            #current variable is still pointing to head of the list
            if current == key and current is self.head:
                found = True 
                self.head = current.next_node #points to second node in the list

            #2nd scenario: key matches the node that's not the heads
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            #3rd scenario: current node we are evaluating does not contain the data that matches the key
            #Make previous node point to the current node and then
            #set current to the next node
            else:   
                previous = current
                current = current.next_node
        #common for remove operations to return the value being removed
        return current

    def __repr__(self):
        """
        Returns a string representation of the list
        Takes O(n) time: Need to traverse the linked list
        """
        """
        To nodes, we're going to add strings that have a description
        that provide a description of each node
        """
        nodes = [] #creating an empty Python list called nodes
        current = self.head #assigning self-head to current; pointer to the head node

        #as long as current does not equal None which means we are not at the tail (end)
        while current:
            #if the node assigned to current is same as the head
            #then we're going to append [Head: %s] to our nodes list
            #current.data refers to the data of the node
            if current is self.head:
                nodes.append("[Head: %s]" % current.data )
            #if next node is None - meaning a tail node
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            #we are not at the tail or the head node
            else:
                nodes.append("[%s]" % current.data)    

            #move the current node forward & reassigning it
            current = current.next_node
        #Joins all the strings thats inside the nodes list together using join method
        return '-> '.join(nodes)



l = LinkedList()
l.add(1)
print(l.size())

l.add(2)
l.add(3)
print(l.size())
print(l)
#output: [Head: 3]-> [2]-> [Tail: 1]


print(l.search(3))