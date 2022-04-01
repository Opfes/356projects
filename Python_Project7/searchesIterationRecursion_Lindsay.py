# Course: CSCI 356, Section 1
# Student Name: Drew Lindsay
# Student ID: 10725791
# Program 5
# Due Date: 4/1/2022
# In keeping with the Honor Code of UM, I have neither given nor received inappropriate assistance
# from anyone other than the TA or instructor.
# Program Description: The following program employs 4 different ways to search for values in an array.
# The first two are sequential, with the first iterating through the array one by one,
# and the second doing so recursively. The other two are designed to work on a list that has
# been sorted, and then performs the same type of searches as the other two, just working
# with the assumping that the list is in order, so it starts with the middle and then
# compares to the value it is searching for, and chooses a side to search.

def sequential_iteration(arr, x):
    #iterate through list
    for y in arr:
        #compare value in array at current index to provided value
        if(y == x):
            return True
    #defaults to return false
    return False


def sequential_recursion(arr, x, index):
    #base case for recursion
    if(index < len(arr)):
        #see if current value is the one we are looking for
        if(arr[index] == x):
            return True
        #if not, run the function again, at an index one higher than before
        else:
            return sequential_recursion(arr, x, index+1)
    #defaults to returning false
    else:
        return False


def binary_iteration(arr, x):
    #first and last indexes
    low = 0
    high = len(arr) - 1
    #while we haven't reached the end of the array
    while low <= high:
        mid = (high + low) // 2
        #if x is higher then the left side of the array is not searched
        if arr[mid] < x:
            low = mid + 1
        #if x is less than, the right of the array is not searched
        elif arr[mid] > x:
            high = mid - 1
        #if x is found in the center, return true
        else:
            return True
    #defaults to false if it doesn't find the index and return true
    return False


def binary_recursion(arr, low, high, x):
    #base case for recursion
    if high >= low:
        mid = (high + low) // 2
        #return true if x is the center value
        if arr[mid] == x:
            return True
        #if middle value is higher than x, then it can only exist on the right side
        elif arr[mid] > x:
            return binary_recursion(arr, low, mid - 1, x)
        #if middle value is lower than x, then it can only exist on the left side
        else:
            return binary_recursion(arr, mid + 1, high, x)
     #defaults to false if it doesn't find the index and return true
    else:
        return False

#array definition for print statements
arr = [1, 3, 5, 7, 9]

print("Sequential Searches:")

#iterative sequential search for 5 and 2 respectively
print("Iteration:", sequential_iteration(arr, 5))
print("Iteration:", sequential_iteration(arr, 2))

#recursive sequential search for 5 and 2 respectively
print("Recursive:", sequential_recursion(arr, 5, 0))
print("Recursive:", sequential_recursion(arr, 2, 0))

print()

print("Binary Searches:")

#iterative binary search for 5 and 2 respectively
print("Iteration:", binary_iteration(arr, 5))
print("Iteration:", binary_iteration(arr, 2))

#recursive binary search for 5 and 2 respectively
print("Recursive:", binary_recursion(arr, 0, len(arr)-1, 5))
print("Recursive:", binary_recursion(arr, 0, len(arr)-1, 2))