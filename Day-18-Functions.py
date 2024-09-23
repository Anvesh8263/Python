# function is a block of code that performs a specific task whenever it is called
# functions are of two types 
#  1. Built in function
#  2. User defined function
def calculateGmean(a,b):
    mean = (a*b)/(a+b)
    print(mean)

def isGreater(a,b):
   if(a>b):
    print("First Number is Greater")
   else:
    print("Second Number is Greater")

a = 9
b = 10
isGreater(a,b)

calculateGmean(a,b)
# gmean = (a*b)/(a+b)
# print(gmean)
c= 8
d=7
if(c>d):
    print("First Number is Greater")
else:
    print("Second Number is Greater")
calculateGmean(c,d)
# gmean1 = (c*d)/(c+d)
# print(gmean1)
