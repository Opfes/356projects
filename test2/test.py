counter=0

def myTest(x):
      if x < 8:
            return (2 * x)
      else:
            return (3 * myTest(x - 8) + 8)

print(myTest(15))