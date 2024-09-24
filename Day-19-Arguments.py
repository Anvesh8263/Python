# There are four types of Arguments
#  1. Default Arguments
#  2. Keywords Arguments
#  3. Variable Arguments
#  4. Required Arguments

def average(a=9,b=1):
    print("The Average is",(a+b)/2)

average(4,6)
average(b=9)

def name(fname, mname = "Anvesh", sname = "Mangalam"):
    print("Hello",fname,mname,sname)

name("Mr.")


def average(*numbers):
    sum=0
    for i in numbers:
        sum = sum+i
    print("Average is: ", sum/len(numbers))

average(5,6)