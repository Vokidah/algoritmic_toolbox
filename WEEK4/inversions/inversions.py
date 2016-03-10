# Uses python3
import sys


def get_number_of_inversions(a, b):
    number_of_invertions = 0
    result = []
    while a and b:
        a_ = a[0]
        b_ = b[0]
        if a_ > b_:
            result.append(b_)
            number_of_invertions += len(a)
            b.remove(b_)
        else:
            result.append(a_)
            a.remove(a_)
    while a:
        a_ = a[0]
        a.remove(a_)
        result.append(a_)
    while b:
        b_ = b[0]
        b.remove(b_)
        result.append(b_)
    return result, number_of_invertions


def merge_sort(a, number_of_inversions):
    if len(a) == 1:
        return a, number_of_inversions
    m = int(len(a)/2)
    b = merge_sort(a[:m], number_of_inversions)
    c = merge_sort(a[m:], number_of_inversions)
    _a, inversions = get_number_of_inversions(b[0], c[0])
    number_of_inversions += inversions+b[1]+c[1]
    return _a, number_of_inversions


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(merge_sort(a, 0)[1])
