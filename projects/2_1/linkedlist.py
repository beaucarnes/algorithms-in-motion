'''
DO IT! CHALLENGE - 2.1 Linked List
Finish the add, remove, and search functions so this LinkedList will work.
To check your work, run 'contactapp.py' and test if all the functions
listed in the menu work correctly.
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def add(self, data):
        # Insert new node as head node

    def remove(self, name):
        # Go through entire list until node to remove is found
        # Once found set previous.next to equal current.next
        # Remember to check if current.data['name'] == name
        # Put your code between 'found = False' and 'return found'
        current = self.head
        previous = None
        found = False





        return found

    def search(self, name):
        # Go through entire list until node is found
        # Return full data of node once found, else return None
        current = self.head
        found = False


