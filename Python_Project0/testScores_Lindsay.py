# Course: CSCI 356, Section 1
# Student Name: Drew Lindsay
# Student ID: 10725791
# Program 0
# Due Date: N/A
# In keeping with the Honor Code of UM, I have neither given nor
# received assistance from anyone other than the TA or the instructor.
# Program description: This program shows how to implement loops and perform some different types of math functions

numberStudents = int(input("Enter the number of students: "))
numberTests = int(input("Enter the number of tests: "))

for x in range(numberStudents):
    print("Student", x+1)
    testTotal = 0
    for i in range(numberTests):
        testTotal += int(input("\tScore for test {}: ".format(i+1)))
    testTotal = round(testTotal/numberTests, 2)
    print("Average for student",x+1,":",testTotal)
    print("-----------------------\n")
