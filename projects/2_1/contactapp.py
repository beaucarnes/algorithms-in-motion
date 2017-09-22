'''
DO IT! CHALLENGE - 2.1 Linked List
Do not modify this file. Finish the Linked List in 'linkedlist.py'.
To check your work, run this file and test if all the functions
listed in the menu work correctly.
'''

import linkedlist

def print_menu():
    print('1. Print Contacts')
    print('2. Add a Contact')
    print('3. Remove a Contact')
    print('4. Lookup a Contact')
    print('5. Quit')
    print('')

people = linkedlist.LinkedList()
people.add({'name' : 'Judah', 'age' : 2})
people.add({'name' : 'Beau', 'age' : 33})
people.add({'name' : 'Aditya', 'age' : 29})

menu_choice = 0
print_menu()
while menu_choice != 5:
    menu_choice = int(input("Type in a number (1-5): "))
    if menu_choice == 1:
        person = people.head
        while person != None:
            print(person.data)
            person = person.next
        print('')
    elif menu_choice == 2:
        print("Add Contact")
        name = raw_input("Name: ")
        age = raw_input("Age: ")
        people.add({'name' : name, 'age' : int(age)})
    elif menu_choice == 3:
        print("Remove Contact")
        name = raw_input("Name: ")
        if people.remove(name):
            print(name + " was deleted")
        else:
            print(name + " was NOT found")
    elif menu_choice == 4:
        print("Lookup Contact")
        name = raw_input("Name: ")
        person = people.search(name)
        if person:
            print(person)
        else:
            print(name + " was not found")
    elif menu_choice != 5:
        print_menu()