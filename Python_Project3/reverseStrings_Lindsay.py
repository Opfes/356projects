# Course: CSCI 356, Section 1
# Student Name: Drew Lindsay
# Student ID: 10725791
# Program 3
# Due Date: 2/25/2022
# In keeping with the Honor Code of UM, I have neither given nor received inappropriate assistance
# from anyone other than the TA or instructor.
# Program Description: A program that has a predefined input, that imports 2 different stack implementations, and then utilizes tham to invert
# a string. It then finds the time it takes for the operations to be completed

#timer import
import timeit
#imports for both stack implementations
from stackA import Stack as StackA
from stackB import Stack as StackB

#StackA implementation function
def reverseString1(givenString):
    #instantiate stack object from StackA class
    Stack1 = StackA()
    #holder for the string once it's reversed
    reversedString = ''
    #iterate through the string and push it character by character onto the stack
    for i in givenString:
        Stack1.push(i)
    #pop values one by one off of the stack and append them to the end of the string using concatenation
    for i in range(Stack1.size()):
        reversedString += Stack1.pop()
    return reversedString

#StackB implementation
def reverseString2(givenString):
    #instantiate stack object from StackA class
    Stack1 = StackB()
    #holder for the string once it's reversed
    reversedString = ''
    #iterate through the string and push it character by character onto the stack
    for i in givenString:
        Stack1.push(i)
    #pop values one by one off of the stack and append them to the end of the string using concatenation
    for i in range(Stack1.size()):
        reversedString += Stack1.pop()
    return reversedString

#hardcoded string to reverse
inputString = "Python programming is fun"
#increased size test string for timing purposes
testString = inputString * 100

#timer implementations for both of the functions, one for each function
t1 = timeit.Timer('reverseString1(testString)', 'from __main__ import reverseString1, testString')
t2 = timeit.Timer('reverseString2(testString)', 'from __main__ import reverseString2, testString')

#main method
def main():
    #print the reversed string using StackA
    print(reverseString1(inputString))
    #print the reversed string using StackB
    print(reverseString2(inputString))
    #print time taken for the StackA implementation
    print("\nTime for reverseString1 is",t1.timeit(1000))
    #print time taken for the StackB implementation
    print("Time for reverseString2 is",t2.timeit(1000))

#call the main method
main()