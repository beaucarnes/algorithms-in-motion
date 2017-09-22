# SPOILER ALERT: Contains solution to 2.1 challenge. Solve that challenge before looking at this code.

# Selection sort is implemented at the end of the LinkedList class.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.length = 0

    def add(self, data):
        temp = Node(data)
        temp.next = self.head
        self.head = temp
        self.length += 1

    def remove(self, name):
        current = self.head
        previous = None
        found = False
        while current != None and not found:
            if current.data['name'] == name:
                found = True
            else:
                previous = current
                current = current.next
        if found:
            if previous == None:
                self.head = current.next
            else:
                previous.next = current.next
        return found

    def search(self, name):
        current = self.head
        found = False
        while current != None and not found:
            if current.data['name'] == name:
                found = True
            else:
                current = current.next
        return current.data if found else None

    def selectionSort(self, sort_by):
        node1 = self.head
        while node1 != None :
            min = node1
            node2 = node1
            while node2 != None :
                if min.data[sort_by] > node2.data[sort_by] :
                    min = node2
                node2 = node2.next
            temp = node1.data
            node1.data = min.data
            min.data = temp
            node1 = node1.next


