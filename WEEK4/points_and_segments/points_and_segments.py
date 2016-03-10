# Uses python3
import sys
import random


def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    starts.sort()
    ends.sort()
    for i in range(0, len(points)):
        lower = for_lower(starts, points[i])
        upper = for_upper(ends, points[i])
        cnt[i] += lower - upper
    return cnt


def for_lower(array, x):
    j = binary_search(array, 0, len(array), x)
    while j < len(array) and array[j] == x:
        j += 1
    return j


def for_upper(array, x):
    j = binary_search(array, 0, len(array), x)
    if j >= len(array):
        return j
    if array[0] == x:
        return 0
    if array[j] != x:
        if array[j-1] == x:
            j -= 1
        else:
            return j
    if array[j] == x and array[j-1] != x:
        return j
    while array[j] == x:
        j -= 1
    return j + 1


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


def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    cnt = fast_count_segments(starts, ends, points)
    for i in cnt:
        print(i, end=' ')