num = [3,2,1,5,4,6]

val = list(map(lambda x:x*2, num))
print(val)

val = list(filter(lambda x:x%2==0, num))
print(val)

print(sorted(num))
# to print the list in reverse order

print(num[::-1])