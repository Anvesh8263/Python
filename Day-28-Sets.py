# Sets can't be take repeated values
#  Sets are unordered collection of data items
#  order ki koi guranteee nhi hai kahi bhi koi bhi aa jata hai
#  we start a dictionary or set with a curly bracket


s = {2,4,2,6}
print(s)

info = {"Anvesh", 23, "Shailendra", 23,44,99}
print(info)

Anvesh = set() # it is set or empty set
print(type(Anvesh))

Anvesh = {} # it is a dictionary
print(type(Anvesh))

for value in info:
    print(value)