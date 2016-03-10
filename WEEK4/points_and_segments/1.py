string = input()
hash = {}
n = len(string)
flag = False
for each in string:
    if each in hash:
        hash[each] += 1
    else:
        hash[each] = 1
array = []
for each in hash:
    array.append(hash[each])
array.sort()
print(hash)
print(array)
if array[-1] - array[0] > 1:
    flag = True
elif array[-2] - array[1] != 0:
    flag = True

if flag:
    print("NO")
else:
    print("YES")