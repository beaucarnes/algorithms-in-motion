# DO IT! CHALLENGE - 2.1 Linked List
# Contact management app implemented using an array (technically a Python list).

def print_menu():
    print('1. Print Contacts')
    print('2. Add a Contact')
    print('3. Remove a Contact')
    print('4. Lookup a Contact')
    print('5. Quit')
    print('')

people = [{'name' : 'Judah', 'age' : 2}, {'name' : 'Beau', 'age' : 33}, {'name' : 'Aditya', 'age' : 29}]

menu_choice = 0
print_menu()
while menu_choice != 5:
    menu_choice = int(input("Type in a number (1-5): "))
    if menu_choice == 1:
        for person in people:
            print(person)
        print('')
    elif menu_choice == 2:
        print("Add Contact")
        name = raw_input("Name: ")
        age = raw_input("Age: ")
        people.append({'name' : name, 'age' : int(age)})
    elif menu_choice == 3:
        print("Remove Contact")
        name = raw_input("Name: ")
        removed = False
        for person in people :
            if person['name'] == name :
                people.remove(person)
                removed = True
        if removed:
            print(name + " was deleted")
        else:
            print(name + " was NOT found")
    elif menu_choice == 4:
        print("Lookup Contact")
        name = raw_input("Name: ")
        found = False
        for person in people :
            if person['name'] == name :
                print(person)
                found = True
        if not found:
            print(name + " was not found")

    elif menu_choice != 5:
        print_menu()