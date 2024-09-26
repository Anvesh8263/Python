# sets are unordered and dictionaries are ordered

ep1 = {122:45,123:89,567:69,679:87}
ep2 = {222:67,455:76}
ep1.update(ep2)
ep1.clear()
print(ep1)
empt = {}
print(empt)
ep1.pop(122)
ep1.popitem()
del ep1[122]
