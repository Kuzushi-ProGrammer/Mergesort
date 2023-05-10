
import time
import random


def sort(array):
    if len(array) <= 1:
        return print("done but len")

    midpoint = len(array) // 2
    leftArray = array[:midpoint] # very confused, real
    rightArray = array[midpoint:]

    print(array)
    print(f"L {leftArray}, R {rightArray}")

    sort(leftArray)


def merge(array1, array2):
    #merge arrays here
    pass

array = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

midpoint = len(array) // 2

leftArray = array[:midpoint]
rightArray = array[midpoint:]

sort(leftArray)
sort(rightArray)

#merge()



