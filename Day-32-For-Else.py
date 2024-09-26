# We can use else with for and while loop both



for i in range(5):
    print(i)
else:
    print("Sorry no i")


for i in []:
    print(i)
else:
    print("Sorry no i")


for i in range(6):
    print(i)
    if i ==5:
        break
else:
    print("Sorry no i ")