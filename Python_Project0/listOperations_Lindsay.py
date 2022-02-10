# Course: CSCI 356, Section 1
# Student Name: Drew Lindsay
# Student ID: 10725791
# Program 0
# Due Date: N/A
# In keeping with the Honor Code of UM, I have neither given nor
# received assistance from anyone other than the TA or the instructor.
# Program description: This program shows how to implement and perform operations on lists

listSize = int(input("Enter number of integers in the list: "))
numberList = []
listSum = 0

for x in range(listSize):
    userNumber = int(input("Enter an integer: "))
    numberList.append(userNumber)

for x in numberList:
    listSum += x

listAverage = round(listSum/len(numberList), 2)

print("The input list is",numberList)
print("The sum of the integers in the list is",listSum)
print("The average of the integers in the list is", listAverage)

numberList.sort()
highestNumber = numberList[len(numberList)-1]
print("The max integer in the list is",highestNumber)