'''
DO IT! CHALLENGE - 3.1 Recursion

SOLUTION
'''

def sort(list, sort_by, startIndex = 0):
    if (startIndex >= len(list) - 1):
        return
    minIndex = startIndex
    for j in range(startIndex + 1, len(list)):
        if list[j][sort_by] < list[minIndex][sort_by]:
            minIndex = j
    temp = list[startIndex]
    list[startIndex] = list[minIndex]
    list[minIndex] = temp
    sort(list, sort_by, startIndex+1)

