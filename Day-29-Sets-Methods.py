s1 = {1,2,5,6}
s2 = {3,6,7,4}
print(s1.union(s2))
print(s1.intersection(s2))

s1.update(s2)
print(s1,s2)


cities  = {"Tokyo","Australia","Dubai"}
cities1 = {"Kabul","India","Australia"}
cities3 = cities.intersection(cities1)
cities3 = cities.symmetric_difference(cities1)
cities3 = cities.difference(cities1)
print(cities3)