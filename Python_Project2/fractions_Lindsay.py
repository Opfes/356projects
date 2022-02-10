class Fraction:
    def __init__(self,upper,lower):
        self.numerator = upper
        self.denominator = lower

    def __str__(self):
        return str(self.numerator) + '/' + str(self.denominator)

    def __add__(self,f2):
        finalNum = self.numerator*f2.denominator + self.denominator*f2.numerator
        finalDen = self.denominator*f2.denominator
        common = gcd(finalNum, finalDen)
        return Fraction(finalNum//common,finalDen//common)

    def __sub__(self,f2):
        finalNum = self.numerator*f2.denominator - self.denominator*f2.numerator
        finalDen = self.denominator*f2.denominator
        common = gcd(finalNum, finalDen)
        return Fraction(finalNum//common,finalDen//common)
    
    def __mul__(self,f2):
        finalNum = self.numerator*f2.numerator
        finalDen = self.denominator*f2.denominator
        common = gcd(finalNum,finalDen)
        return Fraction(finalNum//common,finalDen//common)

    def __truediv__(self,f2):
        finalNum = self.numerator*f2.denominator
        finalDen = self.denominator*f2.numerator
        common = gcd(finalNum,finalDen)
        if finalDen//common == 1:
            return finalNum
        else:
            return Fraction(finalNum//common,finalDen//common)

def gcd(x,y):
    while x % y != 0:
        oldx = x
        oldy = y
        x = oldy
        y = oldx % oldy
    return y

def main():
    num1 = int(input("Enter numerator of the first fraction: "))
    num2 = int(input("Enter denominator of the first fraction: "))
    num3 = int(input("Enter numerator of the second fraction: "))
    num4 = int(input("Enter denominator of the second fraction: "))

    frac1 = Fraction(num1,num2)
    frac2 = Fraction(num3,num4)
    print("First fraction:",frac1)
    print("Second fraction:",frac2)
    print(frac1,"+",frac2,"=",frac1+frac2)
    print(frac1,"-",frac2,"=",frac1-frac2)
    print(frac1,"*",frac2,"=",frac1*frac2)
    print(frac1,"/",frac2,"=",frac1/frac2)

main()