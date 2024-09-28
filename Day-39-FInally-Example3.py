# try:
#      statements which could Generate 
#      exception 
# except:
#      solution of generated exception 
# finally:
#      block of code which is going to 
#      executed in any situation

def func1():
    try:
        l =[1,5,6,7]
        i = int(input("Enter the index: "))
        print(l[i])
        return 1
    except:
        print("Some Error Occurred")
        return 0
    finally:
        print("I am Always Executed")
    
x= func1()
print(x)