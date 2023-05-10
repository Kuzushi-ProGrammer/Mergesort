
import time
import random


def sort(array):
    midpoint = len(array) // 2
    leftArray = array[:midpoint]
    rightArray = array[midpoint:]

    if len(array) <= 1:
        if leftArray > rightArray: #cannot do leftArray[0] cause its out of range apparently??????
            print("swapping")
            leftArray, rightArray = rightArray, leftArray
        return print("Done")

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



