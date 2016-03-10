# Uses python3
import sys
'''
def binary_search(a, l, r, x):
    index = int((l+r)/2)
    if l > r:
        return l
    elif a[index-1] < x <= a[index]:
        return index
    elif x > a[index]:
        return binary_search(a, index+1, r, x)
    else:
        return binary_search(a, l, index-1, x)

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1
'''

def binary_search(a, l, r, x):
    index = int((l+r)/2)
    if l > r:
        return l
    elif a[index-1] < x <= a[index]:
        return index
    elif x > a[index]:
        return binary_search(a, index+1, r, x)
    else:
        return binary_search(a, l, index-1, x)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a,0, len(a)-1, x), end = ' ')