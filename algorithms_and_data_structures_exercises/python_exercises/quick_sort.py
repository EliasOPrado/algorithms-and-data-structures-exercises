
# sequence: [0, 9, 5, 4, 3, 2, 4, 5, 6, 7, 8, 9, 1]
def quick_sort(sequence):
    #gets the int value of the length of the sequence.
    lenght = len(sequence)
    #if the length int value is 0 return the array/sequence.
    if lenght <= 1:
        return sequence
    else:
        #takes the last item from the sequence BEFORE the loop.
        pivot = sequence.pop()
        #e.g: pivot = [1]  from the sequence list.

    items_greater = []
    items_lower = []

    for item in sequence:
        #loops from the lower item to the higher from thre list
        # since the item is looping 1stnumb, 2ndnum, 3rdnumb... e.g: [0, 9, 5, 4, 3, 2, 4, 5, 6, 7, 8, 9]
        if item > pivot:
            # if item is greater than pivot which is already removed from the end of the sequence... see last comment above.
            items_greater.append(item)
            # the item will be added/appended to the [] items_greater list/array
        else:
            items_lower.append(item)
            # otherwise it will be added
    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)

print(quick_sort([0,9,5,4,3,2,4,5,6,7,8,9,1]))

"""
[items_lower][pivot][items_greater]

[0, 9, 5, 4, 3, 2, 4, 5, 6, 7, 8, 9, 1]

1- [0, 1, 9, 5, 4, 3, 2, 5, 6, 7, 8, 9]

2- [0]

3- [5,4,3,2,5,6,7,8][9][9]

4- [0, 1, 5, 4, 3, 2, 5, 6, 7, 8, 9,9]

5- [5, 4, 3, 2, 5, 6, 7][8][]

6- [0, 1, 5, 4, 3, 2, 5, 6, 7, 8, 9, 9]

7- [5, 4, 3, 2, 5, 6][7][]
 ...
8- [0, 1, 5, 4,3, 2, 5, 6, 7, 8, 9, 9]

9- [][2][3, 4, 5]

10- [0, 1, 2, 3, 4, 4, 5, 5, 6, 7, 8, 9, 9]

"""
