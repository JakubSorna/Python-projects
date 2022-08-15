import random
from typing import List

array = []
array2: list[int] = []
for i in range(10):
    array.append(random.randint(1,100))
    array2.append(random.randint(1, 100))

def bubblesort(array):
    for i in range(len(array)):
        for j in range(len(array)-i-1):
            if array[j]>array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
            else:
                continue
    return array

def quicksort(array):
    low = []
    high = []
    equal = []
    if len(array) > 1:
        pivot = array[len(array)//2]
        for i in array:
            if i < pivot:
                low.append(i)
            if i == pivot:
                equal.append(i)
            if i > pivot:
                high.append(i)
        return (quicksort(low) + equal + quicksort(high))
    else:
        return array
