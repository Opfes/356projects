# Course: CSCI 356, Section 1
# Student Name: Drew Lindsay
# Student ID: 10725791
# Program 0
# Due Date: N/A
# In keeping with the Honor Code of UM, I have neither given nor
# received assistance from anyone other than the TA or the instructor.
# Program description: This program shows how to implement and perform operations on dictionaries

roomnames = {
    "CS101":"3004",
    "CS102":"4501",
    "CS103":"6755",
    "NT110":"1244",
    "CM241":"1411"
}

instructors = {
    "CS101":"Haynes",
    "CS102":"Alvarado",
    "CS103":"Rich",
    "NT110":"Burke",
    "CM241":"Lee"
}

meetingtimes = {
    "CS101":"8am",
    "CS102":"9am",
    "CS103":"10am",
    "NT110":"11am",
    "CM241":"1pm"
}

classNumber = input("Enter a course number: ")
if classNumber in roomnames:
    print("The details for ", classNumber, "are:")
    print("\tRoom Number: ",roomnames[classNumber],"\n\tIntstructor: ",instructors[classNumber],"\n\tMeeting Time: ",meetingtimes[classNumber])
else:
    print("No such class")