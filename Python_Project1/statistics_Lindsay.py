# Course: CSCI 356, Section 1
# Student Name: Drew Lindsay
# Student ID: 10725791
# Program 0
# Due Date: N/A
# In keeping with the Honor Code of UM, I have neither given nor
# received assistance from anyone other than the TA or the instructor.
# Program description: This program shows how to implement and perform operations for statistics, mean, median, and mode

#set up list
listSize = int(input("Enter number of integers in the list: "))
numberList = []

#loop to allow users to input users
for x in range(listSize):
    userNumber = int(input("Enter an integer: "))
    numberList.append(userNumber)

#average function
def mean(numberList):
    listSum = 0
    for x in numberList:
        listSum += x
    return round(listSum/len(numberList), 2)

#mode function
def mode(numberList):
    return max(set(numberList), key=numberList.count)

#median function
def median(numberList):
    numberList.sort()
    middle = (len(numberList) - 1) // 2
    if len(numberList) % 2:
        return numberList[middle]
    else:
        return round(((numberList[middle] + numberList[middle+1])/2), 2)

#prints for previously defined functions
print("The input list is",numberList)
print("The mode in the list is:", mode(numberList))
print("The median in the list is:",median(numberList))
print("The mean in the list is:", mean(numberList))