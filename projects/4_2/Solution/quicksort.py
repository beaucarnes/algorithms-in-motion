'''
DO IT! CHALLENGE - 4.2 Quicksort

SOLUTION
'''

def sort(list, sort_by):
    if len(list) < 2:
        return list
    else:
        pivot = list[0]
        less = [i for i in list[1:] if i[sort_by] <= pivot[sort_by]]
        greater = [i for i in list[1:] if i[sort_by] > pivot[sort_by]]
        return sort(less, sort_by) + [pivot] + sort(greater, sort_by)