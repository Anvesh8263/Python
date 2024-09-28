# The Finally code block is also a part of exception handling . when we handle exception using the try and except block , we can include a finally block at the end . The finally block is always executed , so it is generally used for doing the concluding tasks like closing file resources or closing database or may be ending the program execution with a delightful message.

try:
    l = [1,5,6,7]
    i = int(input("Enter the Index: "))
    print(l[i])
except:
    print("Some error Occurred")
finally:
    print("I am always Executed")