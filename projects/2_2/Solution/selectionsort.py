'''
DO IT! CHALLENGE - 2.2 Selection Sort

SOLUTION
'''

def sort(list, sort_by):
    for i in range (len(list)):
        minIndex = i
        for j in range (i+1, len(list)):
            if list[j][sort_by] < list[minIndex][sort_by]:
                minIndex = j
        if minIndex != i:
            temp = list[i]
            list[i] = list[minIndex]
            list[minIndex] = temp