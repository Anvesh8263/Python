a = input("Enter the Value: ")
print(f"Multiplication table of {a} is:")

try:

    for i in range(1,11):
        print(f"{int(a)} X {i} = {int(a)*i}")

except:
    
    print("Invalid Input")
print("End of Program")