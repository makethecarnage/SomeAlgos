import random


def quicksort(array):
    if len(array) < 2:
        return array
    else:

        pivot = array[0]

        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]

        return quicksort(less) + [pivot] + quicksort(greater)

if __name__ == '__main__':

    array = [4,2,7,5,9,1,6,3]
    print(quicksort(array))
