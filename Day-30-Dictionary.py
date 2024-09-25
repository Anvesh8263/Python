dict={
    "Anvesh":"Human Being",
    "spooon":"Object"


}
print(dict["Anvesh"])



dict  = {
    344 : "Neha",
    453 : "Astha",
    654 : "Shailendra",
    423 : "Ritesh"
}
print(dict[654])



info = {'name':'Anvesh','age':23,'eligible':True}
print(info)
print(info['name'])
print(info.get('age'))
print(info.get('eligible'))
print(info.keys())
print(info.values())

for key in info.keys():
    print(f"The value corresponding to the keys {key} is {info[key]}")

print(info.items())
for key, value in info.items():
    print(f"The value corresponding to the key {key} is {value}")