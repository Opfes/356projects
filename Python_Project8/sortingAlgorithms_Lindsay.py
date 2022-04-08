# Course: CSCI 356, Section 1
# Student Name: Drew Lindsay
# Student ID: 10725791
# Program 7
# Due Date: 4/8/22
# In keeping with the Honor Code of UM, I have neither given nor received inappropriate assistance
# from anyone other than the TA or the instructor.
# Program Description: Program with functions for selection, bubble, insertion, merge and quick sorts. The functions
# take arguments passed to them and print out the sorting as steps. All of these functions are then called in a main
# method, one at a time.

#selection sort
def selectionSort(array, size):
    count = 1
    #for loop to iterate through array
    for i in range(size):
        #method to compare all elements in array and find smallest
        min_idx = i
        for j in range(i + 1, size):
            if array[j] < array[min_idx]:
                min_idx = j
        #swap smallest element with the first in the array
        (array[i], array[min_idx]) = (array[min_idx], array[i])
        #print each step
        print('Pass ' + str(count) + ': ' + str(array))
        count += 1

#bubble sort
def bubbleSort(array):
    count = 1
    n = len(array)
    #iterate through array
    for i in range(n):
        #the final i items in the array are ordered correctly
        for j in range(0, n-i-1):
            #iterate through array, swapping the elements if the current is larger than the next
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
        #print the steps
        print('Pass ' + str(count) + ': ' + str(array))
        count += 1

#insertion sort
def insertionSort(array):
    count = 1
    #iterate number of times there are elements in the array
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        #compare key against all elements to its left until a smaller one if found
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        #position key after smaller element
        array[j + 1] = key
        #print steps
        print('Pass ' + str(count) + ': ' + str(array))
        count += 1

#merge sort
def mergeSort(array):
    #print when splitting
    print("Splitting", array)
    if len(array) > 1:
        #find middle of the array
        mid = len(array) // 2
        #split the array into two halves
        L = array[:mid]
        R = array[mid:]
        #recursively call merge sort on both halves
        mergeSort(L)
        mergeSort(R)
        i = j = k = 0
        #copy to holder arrays
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = R[j]
                j += 1
            k += 1
        #check for elements on either side
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            array[k] = R[j]
            j += 1
            k += 1
    #print merging and output
    print("Merging", array)


def partition(array, start, end):
    #assign value to pivot
    pivot = array[start]
    print('Pivot value: ' + str(pivot))
    #assign high and low values based on passed arguments
    low = start + 1
    high = end

    while True:
        #if value is larger than pivot, it is to the right, then move left
        #make sure not to go past "low" value
        while low <= high and array[high] >= pivot:
            high = high - 1

        # the opposite of the above
        while low <= high and array[low] <= pivot:
            low = low + 1
        #either finds an incorrect value for high and low, or a low value that is higher than "high", which gives a break
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break

    array[start], array[high] = array[high], array[start]
    #prints the values in array after partition
    print('List after partition: ' + str(array))
    return high


#quick sort
def quickSort(array, start, end):
    if start >= end:
        return
    #call partition function
    p = partition(array, start, end)
    #sort elements before and after partition
    quickSort(array, start, p - 1)
    quickSort(array, p + 1, end)


#main method to actually use the sorts
def main():
    #instantiates values for selection sort, and then runs it
    print('Selection Sort')
    data = [5, 1, 4, 2, 3]
    size = len(data)
    selectionSort(data, size)
    #new line
    print()

    #instantiates values for bubble sort, and then runs it
    print('Bubble Sort')
    data = [5, 1, 4, 2, 3]
    bubbleSort(data)
    print()

    #instantiates values for insertion sort, and then runs it
    print('Insertion Sort')
    data = [5, 1, 4, 2, 3]
    insertionSort(data)
    print()

    #instantiates values for merge sort, and then runs it
    print('Merge Sort')
    data = [5, 1, 4, 2, 3]
    mergeSort(data)
    print()

    #instantiates values for quick sort, and then runs it
    print('Quick Sort')
    data = [5, 1, 4, 2, 3]
    quickSort(data, 0, size - 1)

#call main
main()