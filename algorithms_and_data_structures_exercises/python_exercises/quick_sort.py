
def quick_sort(sequence):
    #gets the int value of the length of the sequence
    lenght = len(sequence)
    #if the length int value is 0 return the array/sequence
    if lenght <= 1:
        return sequence
    else:
        #takes the last item from the sequence
        pivot = sequence.pop()

    items_greater = []
    items_lower = []
    #loops from the lower item to the higher from thre list
    for item in sequence:
        #since the item is looping 1,2...
        # if item is greater than pivot which is already removed from the last
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)
    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)

print(quick_sort([0,9,5,4,3,2,4,5,6,7,8,9,1]))

"""
[items_lower][pivot][items_greater]

[0,9,5,4,3,2,4,5,6,7,8,9,1]

1- [0,][1][9,5,4,3,2,5,6,7,8,9]

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
