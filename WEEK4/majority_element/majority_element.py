# Uses python3
import sys

def get_majority_element(a, n):
    hash = {}
    for each in a:
        if each not in hash:
            hash[each] = 1
        else:
            hash[each] += 1
    how_many = int(n/2)
    for each in hash.keys():
        if hash[each] > how_many:
            return each
    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, n) != -1:
        print(1)
    else:
        print(0)
