values = [1, 2, "pragati", 4, 6]

print(values[0])
print(values[-1])
print(values[1:3])
values.insert(4, 5)
print(values)
values.append(7)
print(values)
values.extend([8,9,10])
print(values)
values[2] = "PRAGATI" # this type of updation is not supported in tuple
del values[0]
print(values)

values1 = [1, 3, 5, 9, 12, 24]

# iterate multiple list at same time
print("iterate multiple list at same time")
for a,b in zip(values1, values):
    print(a, b)

# Tuple is same as List but it's immutable
val = (1,2, "Pragati", 4,6)
print(val[-1])
# dict
dic= {1:4, 2:"Integer key", "String key": 3}

print(dic[1])
print(dic[2])
print(dic["String key"])



