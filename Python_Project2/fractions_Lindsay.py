# Course: CSCI 356, Section 1
# Student Name: Drew Lindsay
# Student ID: 10725791
# Program 2
# Due Date: 2/11/2022
# In keeping with the Honor Code of UM, I have neither given nor received inappropriate assistance
# from anyone other than the TA or instructor.
# Program Description: Program to show how to use classes and the functions they contain. The program also has a main function
# that utilizes the function by taking a user's input and then applying the input to the classes.

#class constructor
class Fraction:
    #variables that can be used with self
    def __init__(self,upper,lower):
        self.numerator = upper
        self.denominator = lower

    #custom string output function
    def __str__(self):
        return str(self.numerator) + '/' + str(self.denominator)

    #add function
    def __add__(self,f2):
        finalNum = self.numerator*f2.denominator + self.denominator*f2.numerator
        finalDen = self.denominator*f2.denominator
        common = gcd(finalNum, finalDen)
        return Fraction(finalNum//common,finalDen//common)

    #subtract function
    def __sub__(self,f2):
        finalNum = self.numerator*f2.denominator - self.denominator*f2.numerator
        finalDen = self.denominator*f2.denominator
        common = gcd(finalNum, finalDen)
        return Fraction(finalNum//common,finalDen//common)
    
    #multiply function
    def __mul__(self,f2):
        finalNum = self.numerator*f2.numerator
        finalDen = self.denominator*f2.denominator
        common = gcd(finalNum,finalDen)
        return Fraction(finalNum//common,finalDen//common)

    #division function which accounts for if the denominator is 1
    def __truediv__(self,f2):
        finalNum = self.numerator*f2.denominator
        finalDen = self.denominator*f2.numerator
        common = gcd(finalNum,finalDen)
        if finalDen//common == 1:
            return finalNum
        else:
            return Fraction(finalNum//common,finalDen//common)


#greatest common demoniator function to allow the fractions to be reduced
def gcd(x,y):
    while x % y != 0:
        oldx = x
        oldy = y
        x = oldy
        y = oldx % oldy
    return y

def main():
    #user variables
    num1 = int(input("Enter numerator of the first fraction: "))
    num2 = int(input("Enter denominator of the first fraction: "))
    num3 = int(input("Enter numerator of the second fraction: "))
    num4 = int(input("Enter denominator of the second fraction: "))

    frac1 = Fraction(num1,num2)
    frac2 = Fraction(num3,num4)
    #print statements to output the classes after performing the predefined operations
    print("First fraction:",frac1)
    print("Second fraction:",frac2)
    print(frac1,"+",frac2,"=",frac1+frac2)
    print(frac1,"-",frac2,"=",frac1-frac2)
    print(frac1,"*",frac2,"=",frac1*frac2)
    print(frac1,"/",frac2,"=",frac1/frac2)

#calling main
main()